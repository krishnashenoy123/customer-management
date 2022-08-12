from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        #if we want only some fields then we give
        # fields = ['product', 'customer'] like in brackets
        #if we want all then we just give like this
        fields = '__all__'
