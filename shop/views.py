from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class IndexPage(ListView):
    template_name = 'shop/index.html'
    model = Product
    
    
class DetailPage(DetailView):
    template_name = 'shop/detail.html'
    model = Product
    

class SearchView(ListView):
    """ Search Products """
    
    template_name = 'shop/search.html'
    
    def get_queryset(self):
        return Product.objects.filter(name__icontains = self.request.GET.get('q'))
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context