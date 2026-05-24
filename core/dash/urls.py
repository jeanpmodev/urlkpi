from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pyerrors/", views.pyerrors, name="pyerrors"),
    path("uml/", views.uml, name="uml"),
    path("copy/", views.copy, name="copy"),
]
