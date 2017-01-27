from django.utils import timezone
from django.views.generic import ListView
from productos.models import Products

class Products(ListView):
    model = Products
    context_object_name = 'products_list'
    
    def get_context_data(self, **kwargs):
        context = super(Products, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['user'] = {'name':"John Doe"}
        return context
