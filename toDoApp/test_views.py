import pytest
from rest_framework.test import APIRequestFactory
from rest_framework import status
from toDoApp import models as md
from toDoApp import views as vw


# unit tests for views
@pytest.fixture
def api_factory():
    return APIRequestFactory()


@pytest.mark.django_db
@pytest.mark.parametrize(
   'title, description, status_code', [
        (None, None, status.HTTP_400_BAD_REQUEST),
        ('', None, status.HTTP_400_BAD_REQUEST),
        (None, '', status.HTTP_400_BAD_REQUEST),
        ('', '', status.HTTP_400_BAD_REQUEST),
        (
        """
        This message will be written 3 times.
        This message will be written 3 times.
        This message will be written 3 times.
        """, '', status.HTTP_400_BAD_REQUEST),
        (800, '', status.HTTP_201_CREATED),
        ('hello', 12, status.HTTP_201_CREATED),
        ('hello', '', status.HTTP_201_CREATED),
        ('hello', 'description', status.HTTP_201_CREATED)
   ]
)

def test_create_todo_factory(title, description, status_code, api_factory):
    data = { 
        'title': title, 
        'description': description 
    }
    request = api_factory.post('/todos/', data=data, format='json')
    view = vw.ToDoViewSet.as_view({ 'post': 'create' })
    response = view(request)
    print("view\n")
    print(response)
    assert(response.status_code, status_code)
    assert(md.ToDo.objects.count(), 1)
