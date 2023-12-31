# Generated by Django 4.0.4 on 2023-07-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_content', models.BinaryField()),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user_id', models.IntegerField()),
            ],
        ),
    ]
