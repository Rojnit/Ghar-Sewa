from django.contrib import admin
from django.urls import path, include
from home import views  
urlpatterns = [
    path("", views.index, name="index"),
    path("logout/", views.logout, name='logout'),
    path("login/", views.login_view, name='login_view'),
    path("register", views.register,name='register'),
    path('customer/', views.customer, name='customer'),
    path('plumber/',views.plumber, name="plumber"),
    path('carpenter/', views.carpenter, name="carpenter"),
    path('electrician/', views.electrician, name="carpenter"),
    path('userinfo/<userid>', views.userInfo, name="userInfo"),
    path('profile/', views.view_profile, name="profile_view"),
    path('editprofile/', views.edit_profile, name="editprofile"),
    path('change-password/', views.change_password, name="changepassword"),
    path('serviceprovider/' , views.serviceprovider, name="serviceprovider"),
    path('contact/', views.contact, name="contact"),
    path('profile-service/', views.view_profile_service, name="profile_view"),
    path('editprofile-service/', views.edit_profile_service, name="editprofile"),
    path('change-password-service/', views.change_password_service, name="changepassword"),

    path('create/<int:id>/',views.create_service_request, name='create_service_request'),
    path('request/', views.service_request_list, name='service_request_list'),
    path('update/<int:pk>/', views.update_service_request, name='update_service_request'),
    path('customer-order/', views.customer_order_history, name='customer_order_history'),
    path('find_plumbers/', views.find_plumbers, name='find_plumbers'),
    path('find_carpenters/', views.find_carpenters, name='find_carpenters'),
    path('find_electricians/', views.find_electricians, name='find_electricians'),
    path('review/create/<int:service_request_id>/', views.create_review, name='create_review'),
    path('feedbacks/', views.provider_feedbacks, name='provider_feedbacks'),
    
]
    