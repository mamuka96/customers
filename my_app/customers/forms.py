from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Professions, Customers
from django.contrib.auth.models import User

class CustomersForm(forms.ModelForm):

    class Meta():
        model = Customers
        fields = {'first_name', 'second_name', 'birthdate', 'salary', 'professions', }



class ProfessionsForm(forms.ModelForm):

    class Meta():
        model = Professions
        fields = {'profession_name', }


class RegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta(User):
        model = User
        fields = {
            'username',
            'email',
            'password1',
            'password2',
        }


class LoginForm(AuthenticationForm):

    email = forms.CharField()
    password = forms.CharField()
