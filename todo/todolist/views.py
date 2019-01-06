from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from .models import Todo

# Create your views here.

from django.http import HttpResponse
from django.template.loader import render_to_string


try: date_selection
except NameError: date_selection = "1"

def date(request):
	global date_selection
	date_selection = "1"
	date = request.POST.get('task_date')
	return render(request,"date.html")
	

def task(request):
	global date_selection
	if date_selection == "1":
		date = request.POST.get('task_date')
		date_selection = "0"
		
	else:
		date = request.POST.get('selected_date')
	
	list_task = Todo.objects.all().filter(start_date=date)
	start_date = date
	task_name = request.POST.get('task_name')
	task_description = request.POST.get('task_discription')
	finish_date = request.POST.get('complete_date')
	if task_name is not None and task_description is not None and finish_date is not None:
		Todo.objects.create(task_name=task_name,task_description=task_description, finish_date=finish_date, start_date=start_date)
	return render(request, "task.html",{'list_task_list': list_task,'selected_date': date,'date_selection': date})
	
#def list(request):
	#list_task = Todo.objects.all()
#	html = render_to_string('list.html', {'list_task_list': list_task})
#	return HttpResponse(html)