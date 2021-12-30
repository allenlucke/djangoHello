from rest_framework import serializers
from todo.models import Todo, Users


class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('id',
                  'task',
                  'is_complete',
                  'users_id')


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (
            'id',
            'first_name',
            'last_name',
            'username',
            'password',
            "is_active")
