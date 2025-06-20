# Generated by Django 5.2.1 on 2025-06-04 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='task_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='task_videos/')),
                ('audio', models.FileField(blank=True, null=True, upload_to='task_audio/')),
                ('code', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
