# Generated by Django 4.2.4 on 2023-08-31 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_addcompanyamountpayment_company_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
    ]