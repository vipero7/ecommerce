from django import forms
from .models import Order, OrderItem


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'postal_code', 'city']

class OrderEditForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'phone', 'postal_code', 'city', 'paid', 'progress']

        widgets = {
            'first_name': forms.TextInput( 
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'address': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'phone': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'postal_code': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'city': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            
        }

class OrderItemEditForm(forms.Form):
    quantity = forms.CharField(max_length=2)

