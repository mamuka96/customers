from django.shortcuts import render, HttpResponse
from .models import Customers

def hello_world(request):
    context = {
        'title': 'CUSTOMERS',

        'customers': Customers.objects.all(),
    }
    return render(request, 'customers/index.html', context)
