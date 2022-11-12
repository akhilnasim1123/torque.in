from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from phonenumber_field.formfields import PhoneNumberField

from account.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')


    class Meta:
        model = Account
        fields = ('first_name','last_name','phone','email', 'password1', 'password2')


class AccountAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')


    class Meta:
        email = Account
        fields = ('email', 'password')

    # def clean(self):
    #     if self.is_valid():
    #         email = self.cleaned_data['email']
    #         password = self.cleaned_data['password']
    #         if not authenticate(email=email, password=password):
    #             raise forms.ValidationError('invalid login')
