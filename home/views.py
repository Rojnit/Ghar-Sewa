from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, LoginForm, EditProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from home.models import User,ServiceRequest
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponseForbidden


# Create your views here.

def index(request):
    return render(request,"index.html")


def logout(request):
    return render(request, "logout.html")

def plumber(request):

    userData = User.objects.filter(is_plumber=True)
    data = {
        'userData': userData
    }
    return render(request, "plumber.html",data)

def carpenter(request):

    userData = User.objects.filter(is_carpenter=True)
    data = {
        'userData': userData
    }
    return render(request, "carpenter.html",data)

def electrician(request):

    userData = User.objects.filter(is_electrician=True)
    data = {
        'userData': userData
    }
    return render(request, "electrician.html",data)


def customer(request):
    return render(request,'customer.html')


def serviceprovider(request):
    return render(request,'serviceprovider.html')


def contact(request):
    return render(request,'contact.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            user = form.save()
            msg = 'User created successfully.'
            return redirect('login_view')
        else:
            msg = 'Form is not valid.'
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form, 'msg': msg})

def userInfo(request,userid):
    detail = User.objects.filter(id=userid)[0]
    
    return render(request, "userinfo.html", {'detail':detail})

def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            # Authenticate the user
            user = authenticate(request=request, username=username, password=password)

            if user is not None and user.is_authenticated:
                # Use the login function without providing the 'user' argument
                login(request, user)

                # Check user roles and redirect accordingly
                if user.is_admin:
                    return redirect('adminpage')
                elif user.is_customer:
                    return redirect('customer')
                elif user.is_plumber:
                    return redirect('serviceprovider')
                elif user.is_carpenter:
                    return redirect('serviceprovider')
                elif user.is_electrician:
                    return redirect('serviceprovider')
                else:
                    msg = 'User does not belong to any role.'
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating form'

    return render(request, 'login.html', {'form': form, 'msg': msg})

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile.html', args)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
    

@login_required
def view_profile_service(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'profile_service.html', args)

@login_required
def edit_profile_service(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/profile-service')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile_service.html', args)
    

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request,'profile.html')
        else:
            return redirect(request,'change_password')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)
    
def change_password_service(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request,'profile_service.html')
        else:
            return redirect('change_password_service')
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password_service.html', args)
    



from django.shortcuts import render, redirect
from .models import ServiceRequest, ServiceRequestHistory
from django.contrib.auth.decorators import login_required
from .forms import ServiceRequestForm, ServiceRequestUpdateForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from django.shortcuts import render, redirect, get_object_or_404
@login_required
def create_service_request(request, id):  # Note the 'id' parameter here
    provider = get_object_or_404(User, pk=id)  # Adjust this line according to your model
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.provider = provider  # Associate the provider with the service request
            service_request.save()
            ServiceRequestHistory.objects.create(service_request=service_request, status='Created')
            return redirect('customer_order_history')  # Adjust the redirect as needed
    else:
        form = ServiceRequestForm()
    return render(request, 'create_service_request.html', {'form': form})

@login_required
def customer_order_history(request):
    # Fetch service requests with related service provider information
    service_requests = ServiceRequest.objects.filter(customer=request.user).select_related('provider')
    return render(request, 'customer_order_history.html', {'service_requests': service_requests})


@login_required
def service_request_list(request):
    service_requests = ServiceRequest.objects.all()
    if request.user.is_authenticated:
        # Perform your logic here, for example, filtering service requests
        service_requests = ServiceRequest.objects.filter(provider=request.user)
        return render(request, 'service_request_list.html', {'service_requests': service_requests})
    else:
        # If the user is not authenticated, you might redirect them to a login page
        # Or return a different template
        return redirect('name_of_your_login_route')
     

@login_required
def update_service_request(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    if request.user != service_request.provider:
        return HttpResponseForbidden()  # or a redirect
    if request.method == 'POST':
        form = ServiceRequestUpdateForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestUpdateForm(instance=service_request)
    return render(request, 'update_service_request.html', {'form': form})




def find_plumbers(request):
    address_search = request.GET.get('address_search', '')

    if address_search:
        userData = User.objects.filter(is_plumber=True, address__icontains=address_search)
    else:
        userData = User.objects.filter(is_plumber=True)

    context = {'userData': userData}
    return render(request, 'plumber.html', context)

def find_carpenters(request):
    address_search = request.GET.get('address_search', '')

    if address_search:
        userData = User.objects.filter(is_carpenter=True, address__icontains=address_search)
    else:
        userData = User.objects.filter(is_carpenter=True)

    context = {'userData': userData}
    return render(request, 'carpenter.html', context)  # Ensure you have a 'carpenter.html' template


def find_electricians(request):
    address_search = request.GET.get('address_search', '')

    if address_search:
        userData = User.objects.filter(is_electrician=True, address__icontains=address_search)
    else:
        userData = User.objects.filter(is_electrician=True)

    context = {'userData': userData}
    return render(request, 'electrician.html', context)  # Ensure you have an 'electrician.html' template




@login_required
def create_review(request, service_request_id):
    service_request = get_object_or_404(ServiceRequest, id=service_request_id, customer=request.user, status='completed', reviewed=False)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        # Adjusted to use 'customer' instead of 'user'
        Review.objects.create(service_request=service_request, rating=rating, comment=comment, customer=request.user)
        service_request.reviewed = True
        service_request.save()
        return redirect('customer_order_history')
    else:
        return render(request, 'create_review.html', {'service_request': service_request})

    
from .models import Review
@login_required
def provider_feedbacks(request):
    # Assuming each ServiceRequest has a 'provider' field pointing to the service provider user
    service_requests = ServiceRequest.objects.filter(provider=request.user).values_list('id', flat=True)
    reviews = Review.objects.filter(service_request__in=service_requests).select_related('service_request', 'customer').order_by('-created_at')

    return render(request, 'provider_feedbacks.html', {'reviews': reviews})
