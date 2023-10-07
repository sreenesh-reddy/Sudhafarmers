from django.urls import path
from . import views

urlpatterns = [
    path('w_home', views.index, name="w_home"),
    path("result", views.result, name="result"),
    # path('social_links', views.social_links),
]
