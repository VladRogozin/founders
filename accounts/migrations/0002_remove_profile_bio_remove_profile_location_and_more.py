# Generated by Django 5.2.1 on 2025-06-03 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.CharField(choices=[('avatar1.png', 'Аватар 1'), ('avatar2.png', 'Аватар 2'), ('avatar3.png', 'Аватар 3')], default='avatar1.png', max_length=50),
        ),
    ]
