# questions/tests/test_question_list.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from questions.models import Question, Tag
from datetime import datetime

User = get_user_model()

class QuestionListViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hp', password='testpress')
        
        # Create tags
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')
        
        # Create questions
        self.question1 = Question.objects.create(
            title='First Question', 
            description='Content of the first question', 
            user=self.user,
            created_at=datetime(2022, 1, 1)
        )
        self.question2 = Question.objects.create(
            title='Second Question', 
            description='Content of the second question', 
            user=self.user,
            created_at=datetime(2023, 1, 1)
        )
        self.question1.tags.add(self.tag1)
        self.question2.tags.add(self.tag2)
    
    def test_filter_by_tag(self):
        response = self.client.get(reverse('question_list'), {'tags': 'tag1'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question1.title)
        self.assertNotContains(response, self.question2.title)
    
    def test_filter_by_year(self):
        response = self.client.get(reverse('question_list'), {'year': 2022})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question1.title)
        self.assertNotContains(response, self.question2.title)
    
    def test_search_by_title(self):
        response = self.client.get(reverse('question_list'), {'search': 'First'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.question1.title)
        self.assertNotContains(response, self.question2.title)
    
    def test_sort_by_date_desc(self):
        response = self.client.get(reverse('question_list'), {'sort': 'date'})
        self.assertEqual(response.status_code, 200)
        questions = response.context['questions']
        self.assertGreater(questions[0].created_at, questions[1].created_at)
    
    def test_sort_by_date_asc(self):
        response = self.client.get(reverse('question_list'), {'sort': 'date_asc'})
        self.assertEqual(response.status_code, 200)
        questions = response.context['questions']
        self.assertLess(questions[0].created_at, questions[1].created_at)
