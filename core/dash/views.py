from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Task


def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks_list': tasks
    }
    template = loader.get_template("dash/index.html")
    return HttpResponse(template.render(context, request))

