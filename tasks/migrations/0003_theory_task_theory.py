# Generated by Django 5.2.1 on 2025-06-05 16:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_difficulty_taskanswer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='theory_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='theory_videos/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='theory_audio/')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='theory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.theory'),
        ),
    ]
