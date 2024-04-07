# urls.py
from django.urls import path
from .views import saveEnquiry, saveEnquiryCustomer, saveEnquiryService

urlpatterns = [
    path('saveenquiry/', saveEnquiry, name='saveenquiry'),
    path('saveenquiry-customer/', saveEnquiryCustomer, name='saveenquiry-customer'),
    path('saveenquiry-service/', saveEnquiryService, name='saveenquiry-service'),
]
