# Generated by Django 5.1.3 on 2024-11-20 01:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SWOT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='swot',
            old_name='analysis_period',
            new_name='analysis_period_days',
        ),
    ]
