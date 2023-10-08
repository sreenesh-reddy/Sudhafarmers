from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


<<<<<<< HEAD


# class FarmerRegistrationForm(UserCreationForm):
#     farm_name = forms.CharField(max_length=100)

#     class Meta:
#         model = FarmerProfile
#         fields = ('username', 'password1', 'password2', 'email', 'farm_name')

# class ConsumerRegistrationForm(UserCreationForm):
#     favorite_food = forms.CharField(max_length=50)

#     class Meta:
#         model = ConsumerProfile
#         fields = ('username', 'password1', 'password2', 'email', 'favorite_food')
=======
from django.forms import ModelForm
from .models import *
 
class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"
>>>>>>> a7b893903076121cf153aace029db1058825b7af
