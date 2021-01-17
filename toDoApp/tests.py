import pytest
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from toDoApp import models as md
from toDoApp import views as vw
import random


# to integrational tests
@pytest.fixture
def api_client():
   return APIClient()


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
        rand_num = random.randint(100, 1000)
        data = {
            'title': rand_num, 
            'description': '',
        }
        response = self.client.post('/todos/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(md.ToDo.objects.count(), 1)
        self.assertEqual(md.ToDo.objects.get().title, str(rand_num))
        self.assertEqual(md.ToDo.objects.get().description, '')

    def test_create_todo_int_description(self):
        rand_num = random.randint(100, 1000)
        data = {
            'title': 'hello', 
            'description': rand_num,
        }
        response = self.client.post('/todos/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(md.ToDo.objects.count(), 1)
        self.assertEqual(md.ToDo.objects.get().title, 'hello')
        self.assertEqual(md.ToDo.objects.get().description, str(rand_num))
