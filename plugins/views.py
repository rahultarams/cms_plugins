from django.shortcuts import render, redirect,  get_object_or_404
from .models import Properties
# Create your views here.
def property_detail(request, item_id):
    item = get_object_or_404(Properties, pk=item_id)
    request.session['pk'] = item_id
    return render(request, 'sidebar_left.html', {'property': item})