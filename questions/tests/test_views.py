# questions/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from questions.models import Question

User = get_user_model()

class QuestionListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hp', password='testpress')
        self.question = Question.objects.create(title='Test Question', description='Content of the question', user=self.user)
    
    def test_question_list_view(self):
        response = self.client.get(reverse('question_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.title)
        self.assertTemplateUsed(response, 'questions/question_list.html')

    def test_question_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[self.question.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question.title)
        self.assertTemplateUsed(response, 'questions/question_detail.html')
