from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'home.html',{"title":"Home | Farmers Corner"})
def farmers_home(request):
    return render(request, 'farmers_home.html')
def sup(request):
    return render(request, 'signup.html')
def re(request):
    return render(request,'farmers_home.html')
def auth_user(request):
    if request.user.is_authenticated:
        data = {
            'isFarmer': request.user.is_farmer,
            'isWholesaler': request.user.is_wholesaler,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({}, status=403)


def auth_logout(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

def news(request):
    return render(request,'news.html',{"title" : "News"})

def base(request):
    return render(request,'base.html')

def askexp(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'askexp.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addinform.html',context)
 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInDiscussion.html',context)
def viewmore(request,topic):
    try:
        my_object = forum.objects.get(topic=topic)
    except:
        pass
    

    return render(request,'viewmore.html',{'forum':my_object})

from .models import FarmerLogin, WholesalerLogin, ConsumerLogin

def signup(request):
    entity = request.GET.get('entity')
    if request.method == 'POST':
        name = request.POST.get('name')
        aadhar_card_number = request.POST.get('Aadhar')
        
        if entity == 'farmer':
            FarmerLogin.objects.create(name=name, aadhar_card_number=aadhar_card_number)
        elif entity == 'wholesaler':
            WholesalerLogin.objects.create(name=name, aadhar_card_number=aadhar_card_number)
        elif entity == 'consumer':
            ConsumerLogin.objects.create(name=name, aadhar_card_number=aadhar_card_number)

        return redirect('farmers_home')
    
    return render(request, 'signup.html')