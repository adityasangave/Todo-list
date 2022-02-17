from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    task_time = models.DateTimeField(auto_now_add=True)
    task_iscompleted = models.BooleanField()

    def __str__(self):
        return self.task_name