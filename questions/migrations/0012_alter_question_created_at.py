# Generated by Django 5.0.7 on 2024-07-24 10:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_alter_question_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
