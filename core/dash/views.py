from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from .models import Task, Boiler, Service, ErrorManagement, Navbar , CveManagement, Content
from django.http import HttpResponseRedirect, JsonResponse
from pathlib import Path
from operational_micro import *
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.utils import timezone

import os
import time
import re

navbar_list = Navbar.objects.all()


def index(request):
    current_url = request.build_absolute_uri()
    item_list = Service.objects.all().order_by('id')
    paginator = Paginator(item_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    tasks = Task.objects.all()
    service = Service.objects.all()
    context = {
        'tasks_list': tasks,
        'service_list': service,
        'page_obj': page_obj,
        'navbar_list': navbar_list,
        'current_url': current_url,
    }
    template = loader.get_template("dash/index.html")
    return HttpResponse(template.render(context, request))


def boiler(request):
    boiler = Boiler.objects.all()
    current_url = request.build_absolute_uri()
    content = Content.objects.get(content_title='Boiler Plate') 
    if request.user.is_authenticated:

        context = {
            'boiler_list': boiler,
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/boiler.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def copy(request):
    current_url = request.build_absolute_uri()
    content = Content.objects.get(content_title='Copyright Faster') 
    if request.user.is_authenticated:
        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/copy.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def devops(request):
    content = Content.objects.get(content_title='DevOps Center') 
    if request.user.is_authenticated:
        current_url = request.build_absolute_uri()
        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/devops.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def tracking(request):
    content = Content.objects.get(content_title='Data Tracking') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:

        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/tracking.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def filemanager(request):
    content = Content.objects.get(content_title='File Manager') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:

        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/filemanager.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def pyerrors(request):
    content = Content.objects.get(content_title='Detect Pep Errors') 
    current_url = request.build_absolute_uri()
    pep_data = check_pep8()
    error_amount = pep_data["error_amount"]
    list_error_files = pep_data["list_error_files"]
    file_amout = pep_data["file_amout"]
    result = pep_data["result"]
    error_spec = pep_data["error_spec"]
    latest_pep8_checker = ErrorManagement(
        error_type="pep8", error_amount=error_amount, error_datetime=timezone.now())
    latest_pep8_checker.save()

    item_list = Service.objects.all()
    paginator = Paginator(item_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    error_chrono = ErrorManagement.objects.all()
    datetimesdys = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0, '13': 0, '14': 0, '15': 0,
                    '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0, '24': 0, '25': 0, '26': 0, '27': 0, '28': 0, '29': 0, '30': 0, '31': 0}
    for item in error_chrono:
        if (1 <= item.error_datetime.day <= 31):
            datetimesdys[str(item.error_datetime.day)] = item.error_amount
    for key, value in datetimesdys.items():
        print(f"Key: {key}, Value: {value}")

    if request.user.is_authenticated:
        context = {
            'error_amount': error_amount,
            'list_error_files': list_error_files,
            'result': result,
            'error_spec': error_spec,
            'page_obj': page_obj,
            'error_chrono': error_chrono,
            'datetimesdys': datetimesdys,
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/pyerrors.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def plagiarism(request):
    content = Content.objects.get(content_title='Detect Plagiarism') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:

        context = {
            'current_url': current_url,
            'navbar_list': navbar_list,
            'content': content,
        }
        template = loader.get_template("dash/plagiarism.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def integrity(request):
    content = Content.objects.get(content_title='System integrity') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:

        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/integrity.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def tests(request):
    content = Content.objects.get(content_title='Running Tests') 
    current_url = request.build_absolute_uri()
    behave_folder = Path('features/')
    behave_files = [file.name for file in behave_folder.iterdir()
                    if file.is_file()]
    if request.method == 'POST':
        test_name = list(request.POST.keys())[1]
        test_path = os.path.abspath("features/"+test_name)
        try:
            output = subprocess.check_output(
                ['behave', test_path], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
        context = {
        }
        return render(request, 'dash/tests.html', {
            'test_output': output,
            'behave_files': behave_files,
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        })
    if request.user.is_authenticated:
        return render(request, 'dash/tests.html', {
            'behave_files': behave_files,
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        })
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def uml(request):
    content = Content.objects.get(content_title='Software Engineering') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:
        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/uml.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def metadata(request):
    content = Content.objects.get(content_title='Metadata View') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:
        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'content': content,
        }
        template = loader.get_template("dash/metadata.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')


def cybersecurity(request):
    content = Content.objects.get(content_title='Vulnerability Identification') 
    current_url = request.build_absolute_uri()
    if request.user.is_authenticated:
        try:
            output = subprocess.run(
                "rye run pip-audit", shell=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output

    for line in output.stdout:
        print(f"Captured: {line.strip()}")
        context = {
            'navbar_list': navbar_list,
            'current_url': current_url,
            'stdout': output.stdout,
            'stderr': output.stderr,
            'return_code': output.returncode,
            'content': content,
        }
        template = loader.get_template("dash/cybersecurity.html")
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/admin')
