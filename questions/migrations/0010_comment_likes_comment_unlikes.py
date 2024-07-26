# Generated by Django 5.0.7 on 2024-07-24 08:14

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_answer_likes_answer_unlikes'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='liked_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='unlikes',
            field=models.ManyToManyField(related_name='unliked_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]
