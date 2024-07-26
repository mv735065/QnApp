# tests/base_test.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from questions.models import Question, Answer, Comment, Tag
from datetime import datetime

class BaseTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hp', password='testpress')
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')

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

        self.answer1 = Answer.objects.create(
            description='Answer to the first question',
            user=self.user,
            question=self.question1,
            created_at=datetime(2022, 1, 2)
        )

        self.comment1 = Comment.objects.create(
            content='Comment on the answer',
            user=self.user,
            answer=self.answer1,
            created_at=datetime(2022, 1, 3)
        )
