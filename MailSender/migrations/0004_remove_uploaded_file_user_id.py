# Generated by Django 4.0.4 on 2023-07-01 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MailSender', '0003_rename_csv_files_uploaded_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_file',
            name='user_id',
        ),
    ]