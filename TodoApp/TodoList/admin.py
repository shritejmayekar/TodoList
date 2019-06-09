from django.contrib import admin
from TodoList.models import TodoNote,TodoList
# Register your models here.

admin.site.register(TodoNote)
admin.site.register(TodoList)

