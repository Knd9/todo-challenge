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

    def create(self, validated_data):
        return md.ToDo.objects.create(**validated_data)


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
        ids = serializers.ListField(child=serializers.IntegerField(min_value=0))
        model = md.ToDo
        fields = [
            'ids'
        ]

    def validate_completed(self, value, pk):
        if value:
            raise serializers.ValidationError('this To Do with pk'+str(pk)+'is already done. Please rewrite the ids')
        return 1


    def partial_update(self, instance, validated_data):
        if validate_compelted(self, instance.completed, instance.id):# and validate_action(self, validated_data['action']):
            instance.completed = True
            instance.save()
        return instance
