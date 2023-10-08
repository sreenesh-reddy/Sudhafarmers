from django.contrib import admin
from .models import FarmerLogin,ConsumerLogin,WholesalerLogin

admin.site.register(FarmerLogin)
admin.site.register(ConsumerLogin)
admin.site.register(WholesalerLogin)
