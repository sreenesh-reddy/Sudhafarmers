from django.db import models

# Create your models here.
class FarmerProfile(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField()
    farm_name = models.CharField(max_length=10)

    def __str__(self):
        return self.username
    
class ConsumerProfile(models.Model):
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)
    email = models.EmailField()
    favorite_food = models.CharField(max_length=20)

    def __str__(self):
        return self.username
    





class FarmerLogin(models.Model):
    name = models.CharField(max_length=100)
    aadhar_card_number = models.CharField(max_length=12, unique=True)
    def __str__(self):
        return self.name

class WholesalerLogin(models.Model):
    name = models.CharField(max_length=100)
    aadhar_card_number = models.CharField(max_length=12, unique=True)
    def __str__(self):
        return self.name

class ConsumerLogin(models.Model):
    name = models.CharField(max_length=100)
    aadhar_card_number = models.CharField(max_length=12, unique=True)
    def __str__(self):
        return self.name
