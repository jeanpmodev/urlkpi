from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Task
import subprocess
from django.http import HttpResponseRedirect

import os
import pycodestyle
import time


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


def uml(request):
    if request.user.is_authenticated:
        context = {
        }
        template = loader.get_template("dash/uml.html")
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