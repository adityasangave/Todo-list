from cgi import test
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.urls import reverse
from api.serializers import TaskSerializer
from api.models import Task


get_tasks_url = reverse('get')
create_url = reverse('create')

def update_url(id):
    return reverse('update', args=[id])

def delete_url(id):
    return reverse('delete', args=[id])

def details_url(id):
    return reverse('details', args=[id])

def sample_payload():
    payload = {
        "task_name" : "Do homework",
        "task_description" : "Need to complete the homework today",
        "task_iscompleted" : False
    }
    return Task.objects.create(**payload)

class TaskApiTest(TestCase):
    
    def setUp(self):
        self.client = APIClient()

    def test_get_task_list(self):
        res = self.client.get(get_tasks_url)
        
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        payload = {
            "task_name" : "Do homework",
            "task_description" : "Need to complete the homework today",
            "task_iscompleted" : False
        }

        res = self.client.post(create_url, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        task = sample_payload()

        payload = {
            "task_name" : "Do homework",
            "task_description" : "Need to complete the homework today",
            "task_iscompleted" : True
        }

        url = update_url(task.id)
        res = self.client.put(url, payload)

        task.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_delete_task(self):
        task = sample_payload()
        url = delete_url(task.id)

        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_202_ACCEPTED)

    def test_task_details(self):
        task = sample_payload()
        url = details_url(task.id)

        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)