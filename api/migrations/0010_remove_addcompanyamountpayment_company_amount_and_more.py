# Generated by Django 4.2.4 on 2023-09-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_company_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addcompanyamountpayment',
            name='company_amount',
        ),
        migrations.AddField(
            model_name='addcompanyamountpayment',
            name='company_amount_received',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=19),
        ),
    ]
