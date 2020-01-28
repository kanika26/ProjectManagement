from django.contrib import admin
from .models import userlogin, project, task, message
# Register your models here.

admin.site.register(userlogin)
admin.site.register(project)
admin.site.register(task)
admin.site.register(message)