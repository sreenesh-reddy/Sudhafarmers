#from .forms import FarmerRegistrationForm, ConsumerRegistrationForm
from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.
def home(request):
    return render(request,'home.html',{"title":"Home | Farmers Corner"})
def farmers_home(request):
    return render(request, 'farmers_home.html')

def sup(request):
    return render(request, 'signup.html')
from django.http import JsonResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def auth_user(request):
    # Implement your authentication logic here.
    # You can use the request object to access user data.

    if request.user.is_authenticated:
        # Assuming you have a User model with relevant fields like isFarmer and isWholesaler
        data = {
            'isFarmer': request.user.is_farmer,
            'isWholesaler': request.user.is_wholesaler,
        }
        return JsonResponse(data)
    else:
        # User is not authenticated
        return JsonResponse({}, status=403)


def auth_logout(request):
    # Logout the user
    logout(request)
    return JsonResponse({'message': 'Logout successful'})

def news(request):
    return render(request,'news.html',{"title" : "News"})

def base(request):
    return render(request,'base.html')


from .models import FarmerLogin, WholesalerLogin, ConsumerLogin


 
def addInDiscussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            # Retrieve the selected entity type from the form
            entity_type = request.POST.get('entity_type')
            # ... Rest of the registration logic
    else:
        form = ConsumerRegistrationForm()
    return render(request, 'consumer_registration.html', {'form': form})


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
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'viewmore.html',context)

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