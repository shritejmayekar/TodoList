from django.urls import path,include
from django.conf.urls import url
from TodoList.views import TodoNoteViewSet,TodoListViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'todo_note',TodoNoteViewSet)
router.register(r'todo_list',TodoListViewSet)



urlpatterns = [
    path(r'',include(router.urls))
]