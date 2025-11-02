from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

# Create your views here.
@cache_page(60 * 15)
def property_list(request):
    """Return a cached JSON response of all properties."""
    properties = Property.objects.all().values(
        'id', 'title', 'description', 'price', 'location', 'created_at'
    )
    data = list(properties)
    return JsonResponse({'data': data})