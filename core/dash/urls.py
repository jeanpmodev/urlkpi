from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boiler/", views.boiler, name="boiler"),
    path("copy/", views.copy, name="copy"),
    path("filemanager/", views.filemanager, name="filemanager"),
    path("integrity/", views.integrity, name="integrity"),
    path("plagiarism/", views.plagiarism, name="plagiarism"),
    path("pyerrors/", views.pyerrors, name="pyerrors"),
    path("tests/", views.tests, name="tests"),
    path("tracking/", views.tracking, name="tracking"),
    path("uml/", views.uml, name="uml"),

]
