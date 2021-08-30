from django import forms
from .models import Professions, Customers

class CustomersForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    second_name = forms.CharField(max_length=40)
    birthdate = forms.DateField()
    salary = forms.DecimalField(max_digits=10, decimal_places=2)
    professions = forms.ModelChoiceField(queryset=Professions.objects.all())

    def save(self):
        Customers.objects.create(**self.cleaned_data)

    first_name.widget.attrs.update({'class': 'form-control'})
    second_name.widget.attrs.update({'class': 'form-control'})
    birthdate.widget.attrs.update({'class': 'form-control'})
    salary.widget.attrs.update({'class': 'form-control'})
    professions.widget.attrs.update({'class': 'form-select'})

class ProfessionsForm(forms.Form):
    profession_name = forms.CharField(max_length=20)


    def save(self):
        Professions.objects.create(**self.cleaned_data)

    profession_name.widget.attrs.update({'class': 'form-control'})
