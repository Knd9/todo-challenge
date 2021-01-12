from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ToDo
        fields = [
            'id',
            'creationDate',
            'title',
            'description',
            'completed'
        ]
        read_only_fields = ['completed']
