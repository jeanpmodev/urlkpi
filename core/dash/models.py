from django.db import models


class Task(models.Model):
    task_content = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published")
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.task_content} {self.done}"
