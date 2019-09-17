from django.views.generic import View
from django.shortcuts import render
from .models import *

class gallery(View):
    def get(self, request):
        photos = Photo.objects.all()
        return render(request, "gallery.html",  locals())
