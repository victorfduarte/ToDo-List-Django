from django.urls import path
from .views import helloWorld

urlpatterns = [
    path('helloworld/', helloWorld)
]