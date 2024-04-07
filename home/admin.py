from django.contrib import admin
from contact.models import contact
from home.models import User, ServiceRequest,Review
# Register your models here.

admin.site.register(contact)
admin.site.register(User)
admin.site.register(ServiceRequest)
admin.site.register(Review)