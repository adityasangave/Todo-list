from django.test import TestCase
from api import models

class ModelTest(TestCase):

    def test_tag_model_str(self):
        task = models.Task.objects.create(
            task_name = "Do homework",
            task_description = "Need to complete the homework today",
            task_iscompleted = False
        )

        self.assertEqual(str(task), task.task_name)