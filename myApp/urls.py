from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path("",views.helloWorld, name = "helloWorld"),
    path("testpath/", views.testPath, name = "testPath")
]
