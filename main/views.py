from django.views.generic import View
from django.shortcuts import render

class mainView(View):
    def get(self, request):
        return render(request, "mainPage.html")
