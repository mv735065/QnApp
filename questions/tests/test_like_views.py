from .base_test import BaseTest
from django.urls import reverse

class LikeViewsTests(BaseTest):
    def test_like_question_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('like_question', args=[self.question1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.question1.likes.filter(id=self.user.id).exists())

    def test_unlike_question_view(self):
        self.client.login(username='hp', password='testpress')
        response = self.client.post(reverse('unlike_question', args=[self.question1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.question1.unlikes.filter(id=self.user.id).exists())
