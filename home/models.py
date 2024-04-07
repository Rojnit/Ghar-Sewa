from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


def user_profile_picture_path(instance, filename):
    # The file will be uploaded to MEDIA_ROOT/user_<id>/profile_pics/filename
     return f'{instance.username}/profile_pics/{filename}'

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_plumber = models.BooleanField('Is plumber', default=False)
    is_carpenter = models.BooleanField('Is carpenter', default=False)
    is_electrician = models.BooleanField('Is electrician', default=False)
    profilepicture = models.ImageField(upload_to=user_profile_picture_path, null=True, blank=True)
    name = models.CharField('Name', max_length=255, blank=True, null=True)
    address = models.CharField('Address', max_length=255, blank=True, null=True)
    phone = models.CharField('Phone', max_length=20, blank=True, null=True)


    def __str__(self):
        return self.username


class ServiceRequest(models.Model):
    SERVICE_CHOICES = (
        ('plumbing', 'Plumbing'),
        ('carpentry', 'Carpentry'),
        ('electricity', 'Electricity'),
    )
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
        ('completed', 'Completed')
    )


    customer = models.ForeignKey(User, related_name='customer_requests', on_delete=models.CASCADE)
    provider = models.ForeignKey(User, related_name='provider_requests', on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=255, choices=SERVICE_CHOICES)
    description = models.TextField()
    request_time = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.get_service_display()} by {self.customer.username}"


class ServiceRequestHistory(models.Model):
    service_request = models.ForeignKey('ServiceRequest', on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    update_time = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-update_time']

    def __str__(self):
        return f"{self.service_request.id} - {self.status} - {self.update_time}"
    

class Review(models.Model):
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # or a more complex rating system
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.service_request} by {self.reviewer}"
