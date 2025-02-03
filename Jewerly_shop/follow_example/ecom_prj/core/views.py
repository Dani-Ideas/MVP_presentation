from django.conf import settings
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html', {'MEDIA_URL': settings.MEDIA_URL})