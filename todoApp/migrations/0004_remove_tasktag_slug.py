# Generated by Django 4.1.13 on 2024-06-20 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0003_alter_tasktag_unique_together_tasktag_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tasktag',
            name='slug',
        ),
    ]
