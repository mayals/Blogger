# Generated by Django 4.2.9 on 2024-01-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='password1',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='password2',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
