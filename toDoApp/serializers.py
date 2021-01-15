from rest_framework import serializers
from toDoApp import models as md
from django.db import models
from django_filters import rest_framework as filters

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = md.ToDo
        fields = [
            'id',
            'creationDate',
            'title',
            'description',
            'completed'
        ]
        read_only_fields = ['completed']


class ToDoFilter(filters.FilterSet):
    #description_lookup = CharFilter(lookup_expr='icontains', field_name='description', help_text='')
    class Meta:
        model = md.ToDo
        fields = {
            'creationDate': ['exact', 'contains'], 
            'title': ['exact', 'contains'],
            'description': ['exact', 'contains']
        }
        filter_overrides = {
            models.DateTimeField: {'filter_class': filters.DateTimeFilter},
            models.CharField: {'filter_class': filters.CharFilter}
        }
