from django.urls import path
from .views import *

urlpatterns = [
    path('', gallery.as_view(), name="control_orders_url"),
]