# Generated by Django 4.2.7 on 2023-12-20 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_banners_options_alter_enquiry_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainersAchievements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('img', models.ImageField(upload_to='Trainers_Acheievements/')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.trainer')),
            ],
        ),
    ]
