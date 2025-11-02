from django.shortcuts import render
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Property

# Create your views here.
@method_decorator(cache_page(60 * 15), name='dispatch')
class PropertyListView(ListView):
    model = Property
    template_name = 'properties/property_list.html'
    context_object_name = 'properties'

    def get_queryset(self):
        """Return all properties."""
        return Property.objects.all()

