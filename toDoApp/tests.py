import pytest
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework import status
from toDoApp import models as md
from toDoApp import views as vw


# to integrational tests
@pytest.fixture
def api_client():
   return APIClient(enforce_csrf_checks=True)


@pytest.mark.django_db
@pytest.mark.parametrize(
   'title, description, status_code', [
        (None, None, status.HTTP_400_BAD_REQUEST),
        ('', None, status.HTTP_400_BAD_REQUEST),
        (None, '', status.HTTP_400_BAD_REQUEST),
        ('', '', status.HTTP_400_BAD_REQUEST),
        (
        """
        This message will be write 3 times.
        This message will be write 3 times.
        This message will be write 3 times.
        """, '', status.HTTP_400_BAD_REQUEST),
        (800, '', status.HTTP_201_CREATED),
        ('hello', 12, status.HTTP_201_CREATED),
        ('hello', '', status.HTTP_201_CREATED),
        ('hello', 'description', status.HTTP_201_CREATED)
   ]
)
def test_create_todo(title, description, status_code, api_client):
    url = '/todos/'
    data = {
        'title': title,
        'description': description
    }
    response = api_client.post(url, data=data, format='json')
    print(response.data)
    assert response.status_code == status_code
    assert(md.ToDo.objects.count(), 1)


class ToDoTests(APITestCase):
        """
        Ensure we can create a new todo object.
        """
    def test_create_todo_OK(self):
        data = {
            'title': 'todo title', 
            'description': '',
        }
        response = self.client.post('/todos/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(md.ToDo.objects.count(), 1)
        self.assertEqual(md.ToDo.objects.get().title, 'todo title')
        self.assertEqual(md.ToDo.objects.get().description, '')

    def test_create_todo_int_title(self):
        data = {
            'title': 800, 
            'description': '',
        }
        response = self.client.post('/todos/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(md.ToDo.objects.count(), 1)
        self.assertEqual(md.ToDo.objects.get().title, '800')
        self.assertEqual(md.ToDo.objects.get().description, '')

    def test_create_todo_int_description(self):
        data = {
            'title': 'hello', 
            'description': 12,
        }
        response = self.client.post('/todos/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(md.ToDo.objects.count(), 1)
        self.assertEqual(md.ToDo.objects.get().title, 'hello')
        self.assertEqual(md.ToDo.objects.get().description, '12')


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
        This message will be write 3 times.
        This message will be write 3 times.
        This message will be write 3 times.
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
