from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Todo

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TodoSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    class Meta:
        model = Todo
        fields = ['title', 'description', 'created_at', 'id', 'user', 'time_passed']