"""
URL configuration for Sudhafarmers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from farmersco import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',views.base),
    path('',views.home,name='home'),
    path('news/',views.news,name='news'),
    # path('signup/',views.sup),
    path('auth/user/', views.auth_user, name='auth_user'),
    path('auth/logout/', views.auth_logout, name ='auth_logout'),
    path('farmers_home/',views.farmers_home,name='farmers_home'),
    path('signup/', views.signup, name='signup'),
    path('farmers_home/',views.farmers_home),
    path('', include('weather_api.urls')),
    path('askexpert/',views.askexp),
    path('addInForum/',views.addInForum,name='addInForum'),
    path('addInDiscussion/',views.addInDiscussion,name='addInDiscussion'),
    path('viewmore/<str:topic>/',views.viewmore,name='view_more'),
    path('registration/farmer/',views.re)


]
