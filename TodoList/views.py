from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from TodoList.models import Task

from TodoList.serializers import TaskSerializer, TaskValiditySerializer

# Create your views here.
class TaskListAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def post(self, request, *args, **kwargs):
        validator = TaskValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        title = validator.validated_data['title']
        description = validator.validated_data['description']
        completed = validator.validated_data['completed']

        task = Task.objects.create(title=title, description=description, completed=completed)
        task.save()

        return Response(status=status.HTTP_201_CREATED, data={'message': 'Task created successfully'})



class TaskDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        task_detail = self.get_object()
        validator = TaskValiditySerializer(data=request.data)
        if not validator.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': validator.errors})

        task_detail.title = validator.validated_data['title']
        task_detail.description = validator.validated_data['description']
        task_detail.completed = validator.validated_data['completed']
        task_detail.save()
        return Response(status=status.HTTP_201_CREATED, data={'message': 'Task updated successfully'})




