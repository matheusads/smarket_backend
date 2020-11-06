from django.test import TestCase
from rest_framework.test import APIClient
from .models import TaskModel, User


class TestSmartketApi(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='admin')
        self.user2 = User.objects.create(username='smarket')
        self.client = APIClient()

    def test_create_task_model(self):
        TaskModel.objects.create(description='Test', status='C', user_id=self.user.id)
        task = TaskModel.objects.all()[0]
        self.assertEqual(len(TaskModel.objects.all()), 1)
        self.assertEqual(task.user_id, self.user.id)
        self.assertEqual(task.description, 'Test')
        self.assertEqual(task.status, 'C')

    def test_create_task_api(self):
        """Test to create a simple task through endpoint"""
        task_data = {'user_id': self.user.id, 'status': 'D', 'description': 'Test from api'}
        r = self.client.post('/tasks/', task_data)
        self.assertEqual(r.status_code, 201)

    def test_get_all_tasks(self):
        """Test to get all tasks"""
        self.assertEqual(len(TaskModel.objects.all()), 0)  # assert db is clean
        TaskModel(description='Test', status='C', user_id=self.user).save()
        TaskModel(description='Test1', status='P', user_id=self.user2).save()

        r = self.client.get('/tasks/')
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 2)
        self.assertEqual(r.data[0].get('description'), 'Test')
        self.assertEqual(r.data[1].get('description'), 'Test1')

    def test_get_tasks_by_user(self):
        """Test get tasks passing user_id query param"""
        self.assertEqual(len(TaskModel.objects.all()), 0)  # assert db is clean
        TaskModel(description='Test', status='C', user_id=self.user).save()
        TaskModel(description='Test1', status='P', user_id=self.user2).save()

        r = self.client.get(f'/tasks/?user_id={self.user.id}')  # first user/task
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 1)
        self.assertEqual(r.data[0].get('status'), 'C')

        r = self.client.get(f'/tasks/?user_id={self.user2.id}')  # second user/task
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.data), 1)
        self.assertEqual(r.data[0].get('status'), 'P')

    def test_update_task_status(self):
        """Test to update task status like in frontend"""
        task = TaskModel.objects.create(description='Test', status='C', user_id=self.user)
        updated_task = {'description': 'Test', 'status': 'D', 'user_id': self.user.id}
        r = self.client.put(f'/tasks/{task.id}/', data=updated_task)
        self.assertEqual(r.status_code, 200)

    def test_delete_task(self):
        task = TaskModel.objects.create(description='ToDeleted', status='C', user_id=self.user)
        TaskModel.objects.create(description='ToKeep', status='D', user_id=self.user)
        r = self.client.delete(f'/tasks/{task.id}/')
        self.assertEqual(r.status_code, 204)
        self.assertEqual(len(TaskModel.objects.all()), 1)
