from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag, related_name='questions')
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='liked_question', blank=True)
    unlikes = models.ManyToManyField(User, related_name='unliked_question', blank=True)
    # images = models.ManyToManyField('Image', blank=True) 
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super().save(*args, **kwargs)
    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()
    
    def count_answers(self):
        return self.answers.count()

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    likes = models.ManyToManyField(User, related_name='liked_answers')
    unlikes = models.ManyToManyField(User, related_name='unliked_answers')
    # images = models.ManyToManyField('Image', blank=True) 

   

    def count(self):
        question = Question.objects.get(id=self.id)
        return question.answers.count()

    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

    def __str__(self):
        return self.description[:50]

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='replies', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='liked_comments')
    unlikes = models.ManyToManyField(User, related_name='unliked_comments')

    def total_likes(self):
        return self.likes.count()

    def total_unlikes(self):
        return self.unlikes.count()

    def __str__(self):
        return self.content[:50]


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)