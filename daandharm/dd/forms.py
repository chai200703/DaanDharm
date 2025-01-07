from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs = {'class':'form-control'}))
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs = {'class':'form-control'}))
    class Meta:
        model=User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name': 'First Name','last_name':'Last Name','email':'Email'}
        widgets={
            'username':forms.TextInput(),
            'first_name':forms.TextInput(),
            'last_name':forms.TextInput(),
            'email':forms.EmailInput(),
            
        }

class LoginForm(AuthenticationForm):
    username = UsernameField(widget = forms.TextInput())
    password = forms.CharField(label=_("Password"),strip = False, widget = forms.PasswordInput())

class DonationForm(forms.Form):
    DONATION_CHOICES = [
        ('clothes', 'Clothes'),
        ('food', 'Food'),
        ('books', 'Books'),
        ('others', 'Others'),
    ]
    
    donation_type = forms.ChoiceField(
        choices=DONATION_CHOICES, 
        label=_('Type of Donation'), 
        widget=forms.RadioSelect, 
        required=True
    )
    
    full_address = forms.CharField(
        label=_('Full Address'),
        widget=forms.Textarea(attrs={'placeholder': 'Enter your complete address'}),
        max_length=500,
        required=True
    )
    
    pickup_time = forms.TimeField(
        label=_('Preferred Pickup Time'),
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True
    )
