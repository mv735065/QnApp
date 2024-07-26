from .base_test import BaseTest
from django.urls import reverse
from questions.models import *

class CommentViewsTests(BaseTest):
    def test_create_comment_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('create_comment', args=[self.question1.pk]), {
            'content': 'New Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Comment.objects.filter(content='New Comment').exists())

    def test_edit_comment_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('edit_comment', args=[self.question1.pk, self.comment1.pk]), {
            'content': 'Updated Comment'
        })
        self.assertEqual(response.status_code, 302)
        self.comment1.refresh_from_db()
        self.assertEqual(self.comment1.content, 'Updated Comment')
