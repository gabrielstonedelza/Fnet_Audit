# Generated by Django 4.2.4 on 2023-08-30 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='company_whatsapp_phone',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
