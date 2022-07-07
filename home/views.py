from django.shortcuts import render
from . models import *

def home(request):
    products = Products.objects.all()
    context = {
        'products':products,
    }
    return render(request,'index.html',context)