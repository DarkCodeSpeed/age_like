from django.urls import path
from . import views

urlpatterns = [
    path('', views.age_like_view, name='age_like_view'),  # Root URL should be an empty string
    path('success/', views.success_view, name='success'),  # Define the success URL
]
