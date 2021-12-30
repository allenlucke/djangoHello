from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status

from todo.models import Todo, Users
from todo.serializers import TodoSerializer, UsersSerializer


def homePageView(request):
    return HttpResponse("Hello, World!")


# Todos views
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


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return JsonResponse({'message': 'The todo does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        todo_serializer = TodoSerializer(todo)
        return JsonResponse(todo_serializer.data)

    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo_serializer = TodoSerializer(todo, data=todo_data)
        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data)
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'Todo was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def todo_list_completed(request):
    todos = Todo.objects.filter(is_complete=True)

    if request.method == 'GET':
        todo_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(todo_serializer.data, safe=False)


@api_view(['GET'])
def todo_list_is_completed(request, bool):
    bool = bool
    if request.method == 'GET':
        if bool == '0' or bool == 0:
            todos = Todo.objects.filter(is_complete=False)
            todo_serializer = TodoSerializer(todos, many=True)
            return JsonResponse(todo_serializer.data, safe=False)

        elif bool == '1' or bool == 1:
            todos = Todo.objects.filter(is_complete=True)
            todo_serializer = TodoSerializer(todos, many=True)
            return JsonResponse(todo_serializer.data, safe=False)
        else:
            return JsonResponse({'message': 'Hmmmn something is not right! Did you pass something other than a 0 or 1 for the url input?'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['PUT'])
# def todo_flip_is_completed(request, pk):
#     print("In todo_flip_is_completed")
#     try:
#         todo = Todo.objects.get(pk=pk)
#     except Todo.DoesNotExist:
#         return JsonResponse({'message': 'The todo does not exist'}, status=status.HTTP_404_NOT_FOUND)
#
#     # if request.method == 'GET':
#     #     todo_serializer = TodoSerializer(todo)
#     #     return JsonResponse(todo_serializer.data)
#
#     todo_serializer = TodoSerializer(todo)
#
#     print("In todo_flip_is_completed, Last before get")
#
#     todo_serializer.Meta.fields.index()
#
#     if request.method == 'PUT':
#         todo_data = JSONParser().parse(request)
#         todo_serializer = TodoSerializer(todo, data=todo_data)
#         if todo_serializer.is_valid():
#             todo_serializer.save()
#             return JsonResponse(todo_serializer.data)
#         return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Users views
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UsersSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def user_detail(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users_serializer = UsersSerializer(user)
        return JsonResponse(users_serializer.data)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(user, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data)
        return JsonResponse(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def users_list_is_active(request, bool):
    bool = bool
    if request.method == 'GET':
        if bool == '0' or bool == 0:
            users = Users.objects.filter(is_active=False)
            users_serializer = UsersSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)

        elif bool == '1' or bool == 1:
            users = Users.objects.filter(is_active=True)
            users_serializer = UsersSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)

        else:
            return JsonResponse({'message': 'Hmmmn something is not right! Did you pass something other than a 0 or 1 for the url input?'}, status=status.HTTP_204_NO_CONTENT)


# Todos filtered by user
def todo_list_by_user(request, user_id):
    if request.method == 'GET':
        todos = Todo.objects.filter(users_id=user_id)
        todos_serializer = TodoSerializer(todos, many=True)
        return JsonResponse(todos_serializer.data, safe=False)


def todo_list_by_user(request, user_id, is_complete):
    if request.method == 'GET':
        if is_complete == '0' or is_complete == 0:
            todos = Todo.objects.filter(users_id=user_id).filter(is_complete=False)
            todos_serializer = TodoSerializer(todos, many=True)
            return JsonResponse(todos_serializer.data, safe=False)

        elif is_complete == '1' or is_complete == 1:
            todos = Todo.objects.filter(users_id=user_id).filter(is_complete=True)
            todos_serializer = TodoSerializer(todos, many=True)
            return JsonResponse(todos_serializer.data, safe=False)

        else:
            return JsonResponse({'message': 'Hmmmn something is not right! Did you pass something other than a 0 or 1 for the url input?'}, status=status.HTTP_204_NO_CONTENT)
