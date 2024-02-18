from django.urls import path
from .views import *

urlpatterns = [
    path('', handle_form, name='handle_form'),
]