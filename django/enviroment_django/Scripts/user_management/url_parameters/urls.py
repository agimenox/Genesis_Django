from django.urls import path
from . import views

urlpatterns = [
    path('', views.half_number, name='half_number')
]