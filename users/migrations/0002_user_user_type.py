# Generated by Django 4.2.4 on 2023-09-21 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('Administrator', 'Administrator'), ('User', 'User'), ('Customer', 'Customer')], default='User', max_length=100),
        ),
    ]