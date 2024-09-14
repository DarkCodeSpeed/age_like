# views.py
import requests
from datetime import date
from django.shortcuts import render, redirect
from django.db.models import Q
from .forms import UserAgeForm
from .models import UserAge, Like

def get_location_from_ip(ip):
    location_data = {
        "city": "Unknown city",
        "region": "Unknown region",
        "country": "Unknown country",
    }

    services = [
        f"http://ipinfo.io/{ip}/json",
        f"https://ipapi.co/{ip}/json/",
        f"https://freegeoip.app/json/{ip}",
    ]

    for service in services:
        try:
            response = requests.get(service)
            response.raise_for_status()
            data = response.json()

            location_data['city'] = data.get("city", location_data['city'])
            location_data['region'] = data.get("region", location_data['region'])
            location_data['country'] = data.get("country", location_data['country'])

            if location_data['city'] != "Unknown city":
                break

        except requests.exceptions.RequestException as e:
            print(f"Error fetching location from {service}: {e}")

    return location_data

def calculate_age(dob):
    if dob is None:
        return None
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

def age_range(age):
    if age is None:
        return "Unknown"
    if age < 1:
        return "0-1 Years"
    elif age < 2:
        return "1-2 Years"
    elif age < 5:
        return "2-5 Years"
    elif age < 6:
        return "5-6 Years"
    elif age < 10:
        return "6-10 Years"
    elif age < 20:
        return "10-19 Years"
    elif age < 50:
        return "19-49 Years"
    elif age < 60:
        return "49-60 Years"
    else:
        return "60+ Years"

def age_like_view(request):
    if request.method == 'POST':
        user_age_form = UserAgeForm(request.POST)
        if user_age_form.is_valid():
            user_age = user_age_form.save(commit=False)
            user_age.ip_address = request.META.get('REMOTE_ADDR')  # Get IP address
            location_data = get_location_from_ip(user_age.ip_address)  # Get location data from IP
            user_age.city = location_data['city']
            user_age.region = location_data['region']
            user_age.country = location_data['country']
            user_age.device_info = request.POST.get('device_info')  # Get device info from form
            
            # Calculate age from date of birth
            user_age.save()  # Save the user with location, IP, and device info
            Like.objects.create(user_age=user_age)  # Create a like for the user
            return redirect('success')  # Redirect to the success page
    else:
        user_age_form = UserAgeForm()

    total_likes = Like.objects.count()
    users = UserAge.objects.all().order_by('-created_at')

    male_count = users.filter(gender='M').count()
    female_count = users.filter(gender='F').count()
    other_count = users.filter(gender='O').count()
    none_count = total_likes - (male_count + female_count + other_count)

    # Calculate age and age ranges
    age_ranges = {
        "Unknown": 0,
        "0-1 Years": 0,
        "1-2 Years": 0,
        "2-5 Years": 0,
        "5-6 Years": 0,
        "6-10 Years": 0,
        "10-19 Years": 0,
        "19-49 Years": 0,
        "49-60 Years": 0,
        "60+ Years": 0,
    }

    for user in users:
        age = calculate_age(user.date_of_birth)
        age_group = age_range(age)
        age_ranges[age_group] += 1  # Increment the count for the corresponding age group

    search_query = request.GET.get('search', '')
    if search_query:
        users = users.filter(
            Q(name__icontains=search_query) | 
            Q(email__icontains=search_query) | 
            Q(phone__icontains=search_query) |
            Q(username__icontains=search_query)
        )

    return render(request, 'age_like.html', {
        'form': user_age_form,
        'total_likes': total_likes,
        'users': users,
        'search_query': search_query,
        'male_count': male_count,
        'female_count': female_count,
        'other_count': other_count,
        'none_count': none_count,
        'age_ranges': age_ranges,  # Pass age ranges to the template
    })

def success_view(request):
    return render(request, 'success.html', {})