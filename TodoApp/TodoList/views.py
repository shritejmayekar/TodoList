from django.shortcuts import render
from TodoList.models import TodoNote,TodoList
from rest_framework import viewsets
from TodoList.serializers import TodoNoteSerializer,TodoListSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions
# Create your views here.
@api_view(["GET"])
@permission_classes((AllowAny,))
def log(request):
    print(request.user.id)

    return Response('hi')

class TodoNoteViewSet(viewsets.ModelViewSet):
    queryset = TodoNote.objects.all()
    serializer_class = TodoNoteSerializer
    http_method_names = ['get', 'post', 'patch','delete']


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    http_method_names = ['get', 'post', 'patch','delete']


    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
  


