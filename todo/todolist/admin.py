from django.contrib import admin

from .models import task
from .models import date
from .models import Todo
# Register your models here.


admin.site.register(task)
admin.site.register(date)
admin.site.register(Todo)