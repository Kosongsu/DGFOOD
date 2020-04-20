from django.urls import path, include
from .views import client_list, index

urlpatterns = [
    path('', index, name="index"),
    path('client_list', client_list, name="client_list"),

]
