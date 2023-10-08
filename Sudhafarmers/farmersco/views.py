from django.shortcuts import render
from .forms import FarmerRegistrationForm, ConsumerRegistrationForm

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

def farmer_registration(request):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST)
        if form.is_valid():
            # Retrieve the selected entity type from the form
            entity_type = request.POST.get('entity_type')
            # ... Rest of the registration logic
    else:
        form = FarmerRegistrationForm()
    return render(request, 'farmer_registration.html', {'form': form})

def consumer_registration(request):
    if request.method == 'POST':
        form = ConsumerRegistrationForm(request.POST)
        if form.is_valid():
            # Retrieve the selected entity type from the form
            entity_type = request.POST.get('entity_type')
            # ... Rest of the registration logic
    else:
        form = ConsumerRegistrationForm()
    return render(request, 'consumer_registration.html', {'form': form})

