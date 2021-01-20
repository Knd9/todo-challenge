from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from toDoApp import models as md
from toDoApp import serializers as srz


class ToDoViewSet(viewsets.ModelViewSet):
    """
    Provides
    `get`, `filter`, `create`, `update` and `delete` ToDo actions.
    """
    queryset = md.ToDo.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = srz.ToDoFilter
    search_fields = ['^creationDate', 'title', 'description']

    def get_serializer_class(self):
        """
        Return a serializer_class based on the request method
        """
        if self.request.method == 'PATCH':
            return srz.ToDoUpdater
        else:
            return srz.ToDoSerializer

    def get_object(self, pk):
        try:
            return md.ToDo.objects.get(pk=pk)
        except md.ToDo.DoesNotExist:
            raise NotFound('Not found')

    def patch(self, request, pk=None, format=None):
        """
        Update ToDo list to completed
        """
        instances = []
        try:
            ids = request.data.get('id')
            for i in ids:
                todo = self.get_object(i)
                instances.append(todo)
        except (TypeError, ValueError):
            response = {
                'id': 'Invalid format field. Write in [] with positive integers.'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        except NotFound:
            response = {
                'message': 'some to do ID does not exist. Please rewrite the id list.'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        for i in instances:
            i.completed = True
            i.save()
        serializer = srz.ToDoSerializer(instances, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk, format=None):
        """
        Delete a ToDo
        """
        try:
            todo = self.get_object(pk)
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            response = {'message': 'To do with ID ' + pk + \
                ' does not exist. Perhaps it was deleted or it is a negative number'}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
