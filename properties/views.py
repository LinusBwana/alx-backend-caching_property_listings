from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .utils import get_all_properties


@cache_page(60 * 15)
def property_list(request):
    """Return a cached JSON response of all properties."""
    data = get_all_properties()
    return JsonResponse({'data': data})