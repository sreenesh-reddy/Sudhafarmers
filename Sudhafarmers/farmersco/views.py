from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def news(request):
    return render(request,'news.html')

def base(request):
    return render(request,'base.html')