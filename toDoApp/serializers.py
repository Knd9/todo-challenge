from rest_framework import serializers
from django.db import models
from django_filters import rest_framework as filters
from toDoApp import models as md

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

    class Meta:
        model = md.ToDo
        fields = {
            'creationDate': ['year', 'month', 'day', 'hour', 'minute'], 
            'title': ['exact', 'contains'],
            'description': ['exact', 'contains']
        }
        filter_overrides = {
            models.DateTimeField: {'filter_class': filters.DateTimeFilter},
            models.CharField: {'filter_class': filters.CharFilter}
        }


class ToDoUpdater(serializers.ModelSerializer):

    class Meta:
        model = md.ToDo
        fields = [
            'id'
        ]
