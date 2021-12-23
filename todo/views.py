from django.shortcuts import render
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from todo.models import Todo
from todo.serializers import TodoSerializer


def homePageView(request):
    return HttpResponse("Hello, World!")

@api_view(['GET', 'POST', 'DELETE'])
def todo_list(request):
    if request.method == 'GET':
        todos = Todo.objects.all()
        todo_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(todo_serializer.data, safe=False)

    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoSerializer(data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Todo.objects.all().delete()
        return JsonResponse({'message': '{} Todo was deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
