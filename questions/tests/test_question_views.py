# tests/test_question_views.py

from .base_test import BaseTest
from django.urls import reverse
from questions.models import *

class QuestionViewsTests(BaseTest):
    def test_question_list_view(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question1.title)
        self.assertContains(response, self.question2.title)

    # def test_create_question_view(self):
    #     self.client.login(username='hp', password='testpress')
    #     response = self.client.post(reverse('create_question'), {
    #         'title': 'New Question',
    #         'description': 'Content of the new question',
            
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Question.objects.filter(title='New Question').exists())

    def test_question_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[self.question1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question1.title)
        self.assertContains(response, self.answer1.description)
