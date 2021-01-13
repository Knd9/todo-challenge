import pytest
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework import status
from django.urls import reverse
from toDoApp.models import ToDo
from toDoApp.views import ToDoViewSet


# to integrational tests
@pytest.fixture
def api_client():
   return APIClient()

@pytest.mark.django_db
@pytest.mark.parametrize(
   'title, description, status_code', [
        (None, None, 400),
        ('', None, 400),
        (None, '', 400),
        ('', '', 400),
        (
        """
        This message will be write 3 times.
        This message will be write 3 times.
        This message will be write 3 times.
        """, '', 400),
        (800, '', 201),
        ('hello', 12, 201),
        ('hello', '', 201)

   ]
)


def test_create_todo(title, description, status_code, api_client):
    url = '/todos/'
    data = {
        'title': title, 
        'description': description,
    }
    response = api_client.post(url, data=data, format='json')
    print(response.data)
    assert response.status_code == status_code

"""
class ToDoTests(APITestCase):
    def test_create_todo_OK(self):
        
        Ensure we can create a new todo object.
        
        data = {'title': 'new idea'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertEqual(ToDo.objects.get().title, 'new idea')
"""
"""
# to unit tests
@pytest.fixture
factory = APIRequestFactory()


request = factory.post('/todos/', {'title': 'new idea'}, format='json')
assert request.status_code == 201
"""