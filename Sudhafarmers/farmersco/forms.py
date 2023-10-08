from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import FarmerProfile, ConsumerProfile


class FarmerRegistrationForm(UserCreationForm):
    farm_name = forms.CharField(max_length=100)

    class Meta:
        model = FarmerProfile
        fields = ('username', 'password1', 'password2', 'email', 'farm_name')

class ConsumerRegistrationForm(UserCreationForm):
    favorite_food = forms.CharField(max_length=50)

    class Meta:
        model = ConsumerProfile
        fields = ('username', 'password1', 'password2', 'email', 'favorite_food')
