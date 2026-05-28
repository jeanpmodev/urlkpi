from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Task
import subprocess
from django.http import HttpResponseRedirect

import os
import pycodestyle
import time
from pathlib import Path


error_amount = 0
list_error_files = ""
file_amout = 0
result = []
error_spec = []

print(2*"\n")
for dirpath, dirnames, filenames in os.walk("."):
   for filename in filenames:
      if filename.endswith(".py"):
        fchecker = pycodestyle.Checker(dirpath+"/"+filename, show_source=False)
        file_errors = fchecker.check_all()

# quer que compacta em lista pra serializar 


        error_amount += file_errors
        if file_errors != 0:
         file_amout += 1
         list_error_files += filename+"\n"
         print(f"Found {file_errors} errors in "+filename)
         print(100*"  ") 
         #print(filename + "                      ") 
         #time.sleep(1)
result = list_error_files.split()
for item in result:
    item = script_dir = os.path.dirname(os.path.realpath(__file__))
    error_spec = subprocess.run(
        ["pycodestyle", item],
        capture_output=True,  # Captures stdout and stderr
        text=True,            # Returns string instead of bytes
        encoding='utf-8'      # Ensures correct decoding
    )
    error_spec = error_spec.stdout
    error_spec = error_spec.replace(item,"")
    error_spec = error_spec.split('\n')

print(1*"\n")
print("Total files with erros :"+str(file_amout))
time.sleep(1)
print(list_error_files)
time.sleep(1)         
print("Total Errors "+ str(error_amount))

# refatorar funcoes de erros e impressaão 


def index(request):
    tasks = Task.objects.all()

    context = {
        'tasks_list': tasks
    }
    template = loader.get_template("dash/index.html")
    return HttpResponse(template.render(context, request))


def boiler(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/boiler.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def copy(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/copy.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def tracking(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/tracking.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def filemanager(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/filemanager.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def pyerrors(request):
    if request.user.is_authenticated:
        context = {
            'error_amount': error_amount,
            'list_error_files': list_error_files,
            'result': result,
            'error_spec' : error_spec,
        }
        template = loader.get_template("dash/pyerrors.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def plagiarism(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/plagiarism.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def integrity(request):
    if request.user.is_authenticated:

        context = {
        }
        template = loader.get_template("dash/integrity.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def tests(request):
    behave_folder = Path('features/')
    behave_files = [file.name for file in behave_folder.iterdir() if file.is_file()]
    if request.method == 'POST':
        test_name = list(request.POST.keys())[1]
        test_path = os.path.abspath("features/"+test_name)
        try:
            output = subprocess.check_output(['behave', test_path], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output 
        context = {
        }
        return render(request, 'dash/tests.html', {
            'test_output': output,
            'behave_files': behave_files,
        })
    if request.user.is_authenticated:
        return render(request, 'dash/tests.html', {
            'behave_files': behave_files,
        })
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def uml(request):
    if request.user.is_authenticated:
        context = {
        }
        template = loader.get_template("dash/uml.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')

