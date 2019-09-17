from django.urls import path
from .views import *

urlpatterns = [
    path('', mainView.as_view(), name="mainPage"),
]