from django import forms
from .models import Student, Address, Gallery
from .models import Student2, Address2
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model= Student
        fields='__all__'
        exclude = []
    name = forms.CharField(max_length=100,label='Name',required=True,widget=forms.TextInput())
    age = forms.IntegerField(initial=0,label='Age',required=True,widget=forms.NumberInput())
    address=forms.ModelChoiceField(label='City',queryset=Address.objects.all(),required=True, widget=forms.Select())



class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['street', 'city', 'zipcode']
        widgets = {
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'addresses': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }