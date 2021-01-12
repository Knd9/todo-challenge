from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):

    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer 
    #description__name = django_filters.CharFilter(lookup_expr='icontains')
    #filter_backends = [filters.DjangoFilterBackend, filters.SearchFilter]
    #filterset_fields = ['creationDate', 'title', 'description']
    
    @action(detail=True, methods=['post'])
    def registerToDo(self, request, pk=None):
        toDo = self.get_object()
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            toDo.save()
            return Response(serializer.data, 
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
