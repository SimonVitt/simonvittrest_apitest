from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, serializers
from django.core import serializers
from rest_framework import permissions
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.
class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer
    permission_classes = []#[permissions.IsAuthenticated]
    
    def create(self, request):
        todo = Todo.objects.create(title= request.data['title'],
                                   description= request.data['description'],
                                   user= request.user)
        serialized_todo = serializers.serialize('json', [todo])
        return HttpResponse(serialized_todo, content_type='application/json')