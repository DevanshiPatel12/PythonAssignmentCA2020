from django.urls import path
from . import views         # file you're using and file you're invoking should exist in the same directory


urlpatterns = [
    path('', views.index, name = "index"),
]