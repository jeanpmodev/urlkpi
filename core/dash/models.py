from django.db import models


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
    boiler_type = models.CharField(max_length=30, choices=boiler_type, default='Server Side')
    boiler_code = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.boiler_code} {self.boiler_code}"

