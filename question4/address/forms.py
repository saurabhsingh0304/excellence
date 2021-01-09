from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer, Address

class CreateCustomerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'email' ,'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['age']

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields=('street', 'pincode', 'country', 'state', 'phone_num')