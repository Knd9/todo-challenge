from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend, CharFilter
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from toDoApp import models as md
from toDoApp import serializers as srz

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):

    queryset = md.ToDo.objects.all()
    serializer_class = srz.ToDoSerializer 
    filter_backends = [DjangoFilterBackend]
    filterset_class = srz.ToDoFilter
    
    @action(detail=True, methods=['post'])
    def registerToDo(self, request, pk=None):
        toDo = self.get_object()
        serializer = srz.ToDoSerializer(data=request.data)
        if serializer.is_valid():
            toDo.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

   # @action(detail=False, methods=['get'])
   # def listToDos(self, request, pk=None)
