from rest_framework import serializers
from .models import Todo, User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'completed')



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active', 'created', 'updated']