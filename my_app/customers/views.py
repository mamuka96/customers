from django.shortcuts import render, redirect
from django.views import View
from .models import Customers, Professions
from .mixins import *
from .forms import *

class CustomersList(ObjectsListMixin, View):
    model = Customers
    template = 'customers/customers.html'



class ProfessionsList(ObjectsListMixin, View):
    model = Professions
    template = 'customers/professions.html'

class CreatorCustomers(CreatorObjectsMixin, View):
    model = Customers
    template = 'customers/create_customers.html'
    form = CustomersForm

class CreatorProfessions(CreatorObjectsMixin, View):
    model = Professions
    template = 'customers/create_professions.html'
    form = ProfessionsForm








