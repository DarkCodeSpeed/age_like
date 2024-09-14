# forms.py
from django import forms
from .models import UserAge

class UserAgeForm(forms.ModelForm):
    device_info = forms.CharField(widget=forms.HiddenInput(), required=False)  # Hidden input for device info

    class Meta:
        model = UserAge
        fields = ['username', 'name', 'email', 'phone', 'f_name', 'gender', 'date_of_birth']  # Include model fields

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserAge.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if UserAge.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username