# Generated by Django 5.0.2 on 2024-02-29 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_rename_password_password_encrypted_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='password',
            name='key',
        ),
    ]
