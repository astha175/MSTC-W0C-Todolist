from django.urls import path

from . import views

urlpatterns = [
    
	path('date/', views.date, name='date'),
	path('task/', views.task, name='task'),
	#path('list/', views.list, name='list')
]

