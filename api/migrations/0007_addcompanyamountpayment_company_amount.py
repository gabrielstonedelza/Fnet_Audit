# Generated by Django 4.2.4 on 2023-08-30 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_addcompanyamountpayment_unique_identifier'),
    ]

    operations = [
        migrations.AddField(
            model_name='addcompanyamountpayment',
            name='company_amount',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='company_amount', to='api.addcompanyamountreceived'),
        ),
    ]
