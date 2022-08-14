from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Order
from django import forms

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #if we want only some fields then we give
        # fields = ['product', 'customer'] like in brackets
        #if we want all then we just give like this
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']