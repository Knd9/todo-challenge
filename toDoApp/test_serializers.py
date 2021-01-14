import pytest
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from rest_framework import status
from toDoApp import models as md
from toDoApp import views as vw
from toDoApp import serializers as srz


# unit tests
@pytest.fixture
def api_factory():
    return APIRequestFactory()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'title, description, is_valid_value, exception, message', [
        (None, None, False, 'description', ['This field may not be null.']),
        ('', '', False, 'title', ['This field may not be blank.']),
        (
            """
        This message will be write 3 times.
        This message will be write 3 times.
        This message will be write 3 times.
        """, '', False, 'title', ['Ensure this field has no more than 100 characters.']),
    ]
)
def test_create_todo_serializer_exception(
        title, description, is_valid_value, exception, message, api_factory):
    data = {
        'title': title,
        'description': description
    }
    request = api_factory.post('/todos/', data=data, format='json')
    serializer = srz.ToDoSerializer(
        data=data, context={
            'request': Request(request)})
    assert(serializer.is_valid() is is_valid_value)
    assert(serializer.errors[exception] == message)


@pytest.mark.django_db
@pytest.mark.parametrize(
    'title, description, is_valid_value', [
        (800, '', True),
        ('hello', 12, True),
        ('hello', '', True),
        ('hello', 'description', True)
    ]
)
def test_create_todo_serializer_OK(
        title, description, is_valid_value, api_factory):
    data = {
        'title': title,
        'description': description
    }
    request = api_factory.post('/todos/', data=data, format='json')
    serializer = srz.ToDoSerializer(
        data=data, context={
            'request': Request(request)})
    assert(serializer.is_valid() is is_valid_value)
