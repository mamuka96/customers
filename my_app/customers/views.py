from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
from .models import Customers, Professions
from .mixins import *
from .forms import *

class CustomersList(ListView):
    model = Customers
    template_name = 'customers/customers.html'
    extra_context = {'fields': model._meta.fields,
                     }
    paginate_by = 2



class ProfessionsList(ListView):
    model = Professions
    template_name = 'customers/professions.html'
    extra_context = {'fields': model._meta.fields,
                     'objects': model.objects.all(),
                     }
    paginate_by = 2


class CreatorCustomers(CreatorObjectsMixin, View):
    model = Customers
    template = 'customers/create_customers.html'
    form = CustomersForm

class CreatorProfessions(CreatorObjectsMixin, View):
    model = Professions
    template = 'customers/create_professions.html'
    form = ProfessionsForm


class UpdateCustomers(UpdateObjectsMixin,View):

    model = Customers
    template = 'customers/update_customer.html'
    form = CustomersForm

class UpdateProfessions(UpdateObjectsMixin, View):

    model = Professions
    template = 'customers/update_profession.html'
    form = ProfessionsForm

class DeleteCustomers(DeleteObjectsMixin, View):

    model = Customers
    template = 'customers/delete_customer.html'

class DeleteProfessions(DeleteObjectsMixin, View):

    model = Professions
    template = 'customers/delete_profession.html'













