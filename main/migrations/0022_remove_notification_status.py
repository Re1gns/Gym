# Generated by Django 4.2.7 on 2023-12-14 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_notification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='status',
        ),
    ]
