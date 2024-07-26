# tests/test_answer_views.py

from .base_test import BaseTest
from django.urls import reverse
from questions.models import *

class AnswerViewsTests(BaseTest):
    def test_create_answer_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('create_answer', args=[self.question1.pk]), {
            'description': 'New Answer'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Answer.objects.filter(description='New Answer').exists())

    def test_edit_answer_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('edit_answer', args=[self.question1.pk, self.answer1.pk]), {
            'description': 'Updated Answer'
        })
        self.assertEqual(response.status_code, 302)
        self.answer1.refresh_from_db()
        self.assertEqual(self.answer1.description, 'Updated Answer')
