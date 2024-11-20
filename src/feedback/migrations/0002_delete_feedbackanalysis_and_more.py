# Generated by Django 5.1.3 on 2024-11-20 00:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FeedbackAnalysis',
        ),
        migrations.AddField(
            model_name='platformfeedback',
            name='submission_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='platformfeedback',
            name='description',
            field=models.TextField(),
        ),
    ]
