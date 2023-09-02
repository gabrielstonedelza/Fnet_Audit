# Generated by Django 4.2.4 on 2023-09-02 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addcompanyamountreceived',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addcompanyamountreceived',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AddField(
            model_name='addcompanyamountpayment',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='addcompanyamountpayment',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.AddField(
            model_name='addcompanyamountpayment',
            name='company_amount',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_amount', to='api.addcompanyamountreceived'),
        ),
    ]
