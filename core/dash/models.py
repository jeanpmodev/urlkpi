from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class Task(models.Model):
    task_content = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_content} {self.done}"


class Boiler(models.Model):
    boiler_type = [
        ('BackEnd', 'Backend'),
        ('Server Side', 'ServerSide'),
        ('Data Base', 'Database')
    ]
    boiler_type = models.CharField(
        max_length=30, choices=boiler_type, default='Server Side')
    boiler_code = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.boiler_code} {self.boiler_code}"


class Service(models.Model):
    service_name = models.CharField(max_length=50)
    service_link = models.URLField(max_length=300, blank=True)
    service_content = models.CharField(max_length=300, default='Services')
    service_on_content = models.CharField(max_length=300)
    service_off_content = models.CharField(max_length=300)
    service_status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.service_name} {self.service_status}"


class ErrorManagement(models.Model):
    error_type = [
        ('pep8', 'pep8'),
        ('frontend', 'frontend')
    ]
    error_type = models.CharField(
        max_length=20, choices=error_type, default='pep8')
    error_amount = models.IntegerField(default=0)
    error_datetime = models.DateTimeField(default=timezone.now)


class Navbar(models.Model):
    btn_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.CharField(max_length=50, default='bulb-outline')
    title = models.CharField(max_length=100, default='Management')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class CveManagement(models.Model):
    cve_code = models.CharField(max_length=100)
    to_solve = models.URLField(max_length=300, blank=True)
    cve_amount = models.IntegerField(default=0)
    pkg_amount = models.IntegerField(default=0)
    cve_datetime = models.DateTimeField(default=timezone.now)


class Content(models.Model):
    content_title = models.CharField(max_length=100, default="title")
    content_subtitle = models.CharField(max_length=400, default="content")
    content_1 = models.TextField(max_length=400, default="content")
    content_2 = models.TextField(max_length=400, default="content")
    content_3 = models.TextField(max_length=400, default="content")
    content_4 = models.TextField(max_length=400, default="content")
    wizard_1 = models.CharField(max_length=50, default='wizard 1')
    wizard_2 = models.CharField(max_length=50, default='wizard 2')
    wizard_3 = models.CharField(max_length=50, default='wizard 3')
    wizard_4 = models.CharField(max_length=50, default='wizard 4')

