from django.db import models

#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous" )
    topic= models.CharField(max_length=300)
    description = models.CharField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)



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