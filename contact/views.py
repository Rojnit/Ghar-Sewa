
from django.shortcuts import render
from contact.models import contact
def saveEnquiry(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        message=request.POST.get('desc')
        en=contact(firstName=firstname, lastName=lastname, address=address, email=email, description=message)
        en.save()
    return render(request, "index.html")

def saveEnquiryService(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        message=request.POST.get('desc')
        en=contact(firstName=firstname, lastName=lastname, address=address, email=email, description=message)
        en.save()
    return render(request, "serviceprovider.html")

def saveEnquiryCustomer(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        message=request.POST.get('desc')
        en=contact(firstName=firstname, lastName=lastname, address=address, email=email, description=message)
        en.save()
    return render(request, "customer.html")