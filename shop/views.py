from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class IndexPage(ListView):
    template_name = 'shop/index.html'
    model = Product
    
    
class DetailPage(DetailView):
    template_name = 'shop/detail.html'
    model = Product