<<<<<<< HEAD
from django.contrib import admin
from .models import FarmerLogin,ConsumerLogin,WholesalerLogin

admin.site.register(FarmerLogin)
admin.site.register(ConsumerLogin)
admin.site.register(WholesalerLogin)
=======


# Register your models here.
from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(forum)
admin.site.register(Discussion)
>>>>>>> a7b893903076121cf153aace029db1058825b7af
