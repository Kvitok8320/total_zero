from django import forms
from .models import Order
from register.models import User
from catalog.models import Product

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'products']
        widgets = {
            'products': forms.CheckboxSelectMultiple(),
        }