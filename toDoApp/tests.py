import pytest
from rest_framework.test import APIClient, APIRequestFactory, APITestCase
from rest_framework import status
from django.urls import reverse
from toDoApp.models import ToDo


# to integrational tests
@pytest.fixture
client = APIClient()


class ToDoTests(APITestCase):
    def test_create_todo_OK(self):
        """
        Ensure we can create a new todo object.
        """
        url = '/todos/'
        data = {'title': 'new idea'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().title, 'new idea')


# to unit tests
@pytest.fixture
factory = APIRequestFactory()


request = factory.post('/todos/', {'title': 'new idea'}, format='json')
assert request.status_code == 201