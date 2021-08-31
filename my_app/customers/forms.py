from django import forms
from .models import Professions, Customers

class CustomersForm(forms.ModelForm):

    class Meta():
        model = Customers
        fields = {'first_name', 'second_name', 'birthdate', 'salary', 'professions', }





class ProfessionsForm(forms.ModelForm):

    class Meta():
        model = Professions
        fields = {'profession_name',}

