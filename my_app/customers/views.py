import self as self
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Customers, Professions
from .mixins import *
from .forms import *

class CustomersList(ListView):
    model = Customers
    template_name = 'customers/customers.html'
    extra_context = {'fields': model._meta.fields,
                     }
    paginate_by = 2

    def get_queryset(self):

        second_name = self.request.GET.get('search')

        if second_name:
            object_list = self.model.objects.filter(second_name=second_name)
        else:
            object_list = self.model.objects.all()

        return object_list



class ProfessionsList(ListView):
    model = Professions
    template_name = 'customers/professions.html'
    extra_context = {'fields': model._meta.fields,

                     }
    paginate_by = 2

    def get_queryset(self):

        profession_name = self.request.GET.get('search')

        if profession_name:
            object_list = self.model.objects.filter(profession_name=profession_name)
        else:
            object_list = self.model.objects.all()

        return object_list



class CreatorCustomers(LoginRequiredMixin, CreateView):

    raise_exception = True
    model = Customers
    template_name = 'customers/create_customers.html'
    form_class = CustomersForm
    success_url = reverse_lazy('customers-list')



class CreatorProfessions(LoginRequiredMixin, CreateView):

    raise_exception = True
    model = Professions
    template_name = 'customers/create_professions.html'
    form_class = ProfessionsForm
    success_url = reverse_lazy('professions-list')


class UpdateCustomers(LoginRequiredMixin, UpdateView):

    raise_exception = True
    model = Customers
    template_name = 'customers/update_customer.html'
    form_class = CustomersForm
    success_url = reverse_lazy('customers-list')



class UpdateProfessions(LoginRequiredMixin,UpdateView):

    raise_exception = True
    model = Professions
    template_name = 'customers/update_profession.html'
    form_class = ProfessionsForm
    success_url = reverse_lazy('professions-list')

class DeleteCustomers(LoginRequiredMixin, DeleteView):

    raise_exception = True
    model = Customers
    template_name = 'customers/delete_customer.html'
    success_url = reverse_lazy('customers-list')


class DeleteProfessions(LoginRequiredMixin, DeleteView):

    raise_exception = True
    model = Professions
    template_name = 'customers/delete_profession.html'
    success_url = reverse_lazy('professions-list')


class Registration(View):

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'customers/registration.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

        return render(request, 'customers/registration.html', {'form': form})


class Login(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'customers/login.html', {'form': form})


    def post(self, request):

        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.get_user()
            login(request, username)
            return redirect('customers-list')
        else:
            return render(request, 'customers/login.html', {'form': form})














