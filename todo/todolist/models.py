import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class date(models.Model):
    date = models.DateTimeField('date')
	# def was_published_recently(self):
     #   return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class task(models.Model):
	task_name = models.CharField(max_length=200,null=True, blank=True)
	task_description = models.TextField(null=True, blank=True)
	start_date = models.DateField(null=True)
	finish_date = models.DateField(null=True)
	accomplish_date = models.DateField(null=True)

class Todo(models.Model):
	task_name = models.CharField(max_length=200,null=True, blank=True)
	task_description = models.TextField(null=True, blank=True)
	start_date = models.DateField(null=True)
	finish_date = models.DateField(null=True)
	accomplish_date = models.DateField(null=True)