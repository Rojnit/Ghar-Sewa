from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, ServiceRequest
from django.forms.widgets import TimeInput
class LoginForm(forms.Form):
    username = forms.CharField(
        widget= forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    profilepicture = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_admin', 'is_plumber', 'is_carpenter', 'is_electrician', 'is_customer','phone', 'address', 'name', 'profilepicture')
    

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'address',
            'profilepicture',
            'username',
            'phone'
            
        )
        

class ServiceRequestForm(forms.ModelForm):
    provider = forms.ModelChoiceField(
        queryset=User.objects.filter(is_plumber=True) | User.objects.filter(is_carpenter=True) | User.objects.filter(is_electrician=True),
        required=False,
        
    )

    class Meta:
        model = ServiceRequest
        fields = ['service', 'description', 'request_time']
        widgets = {
            'request_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),  # For datetime input
            # 'request_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M'),  # For time-only input, if preferred
        }

    

# Make sure this class is defined if you are trying to import it
class ServiceRequestUpdateForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['status'] # Example fields you might want to update


