from .models import Category, Product
from django import forms
from django.forms import TextInput

#Category Form
class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
        } 


#Product Form
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'available', 'image','description')
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
        } 

class ProductEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'category', 'price', 'available', 'image','description')
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
            'price': forms.TextInput(
                attrs = {
                    'class': 'form-control col-md-7',
                    'style': 'border-color:black',
                }
            ),
        }  