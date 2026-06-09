from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("boilerplate/", views.boiler, name="boiler"),
    path("copyright/", views.copy, name="copy"),
    path("file-management/", views.filemanager, name="filemanager"),
    path("software-integrity/", views.integrity, name="integrity"),
    path("plagiarism/", views.plagiarism, name="plagiarism"),
    path("pep-errors/", views.pyerrors, name="pyerrors"),
    path("tests/", views.tests, name="tests"),
    path("datatracking/", views.tracking, name="tracking"),
    path("uml-management/", views.uml, name="uml"),
    path("devops/", views.devops, name="devops"),
]
