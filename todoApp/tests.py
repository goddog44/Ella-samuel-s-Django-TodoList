from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from .models import Task, Tag

class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.task = Task.objects.create(
            title='Test Task',
            description='Test Description',
            due_date=timezone.now() + timezone.timedelta(days=1),
            user=self.user
        )
        self.tag = Tag.objects.create(name='Test Tag')

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'Test Description')
        self.assertFalse(self.task.is_completed)
        self.assertEqual(self.task.user, self.user)

    def test_task_update(self):
        self.task.title = 'Updated Task'
        self.task.save()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_task_deletion(self):
        self.task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_task_status_update(self):
        self.task.is_completed = True
        self.task.save()
        self.assertTrue(self.task.is_completed)

    def test_tag_assignment(self):
        self.task.tags.add(self.tag)
        self.assertIn(self.tag, self.task.tags.all())