# Generated by Django 5.0.2 on 2024-02-29 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_remove_password_logo_password_key_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='password',
            options={},
        ),
        migrations.AlterField(
            model_name='password',
            name='key',
            field=models.CharField(default='', max_length=255),
        ),
    ]