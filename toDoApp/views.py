from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from toDoApp import models as md
from toDoApp import serializers as srz


class ToDoViewSet(viewsets.ModelViewSet):

    queryset = md.ToDo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = srz.ToDoFilter
    search_fields = ['^creationDate', 'title', 'description']

    def get_serializer_class(self):
        """
        Choice a serializer_class according to the action endpoint
        """
        if self.action == 'partial_update' or self.action == 'update':
            return srz.ToDoUpdater
        else:
            return srz.ToDoSerializer

    def get_object(self, pk):
        try:
            return md.ToDo.objects.get(pk=pk)
        except md.ToDo.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    @action(detail=True, methods=['post'])
    def post(self, request, pk=None):
        todo = self.get_object()
        serializer = srz.ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['patch'])
    def patch(self, request, pk=None, format=None):
        ret = []
        ids = request.data.get('ids')
        for pk in ids:
            todo = self.get_object(pk)
            serializer = srz.ToDoUpdater(todo, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            ret.append(todo)
        return Response(ret)

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
