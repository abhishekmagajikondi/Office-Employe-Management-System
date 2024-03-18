from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path("",views.home , name = 'home'),
    path("viewE",views.viewE , name = 'viewE'),
    path("AddE",views.AddE , name = 'AddE'),
    path("AddDetails",views.AddDetails , name = 'AddDetails'),
    path("RemoveE",views.RemoveE , name = 'RemoveE'),
    path("RemoveEmployee<int:id>",views.RemoveEmployee , name = 'RemoveEmployee'),
    path("FilterE",views.FilterE , name = 'FilterE'),
    path("FilterE1",views.FilterE1, name = 'FilterE1'),
]
