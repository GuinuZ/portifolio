from django.urls import path
from header.views import home

urlpatterns = [
    path('', home)
]
