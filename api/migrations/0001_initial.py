# Generated by Django 4.2.4 on 2023-08-30 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddCompanyAmountPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=19)),
                ('screenshot', models.ImageField(default='screenshot.png', upload_to='screenshots')),
                ('unique_identifier', models.CharField(max_length=255)),
                ('payment_month', models.CharField(blank=True, default='', max_length=10)),
                ('payment_year', models.CharField(blank=True, default='', max_length=10)),
                ('date_paid', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddCompanyAmountReceived',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_received', models.DecimalField(blank=True, decimal_places=2, max_digits=19)),
                ('receipt', models.ImageField(default='receipt.png', upload_to='receipts')),
                ('unique_identifier', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255, unique=True)),
                ('received_month', models.CharField(blank=True, default='', max_length=10)),
                ('received_year', models.CharField(blank=True, default='', max_length=10)),
                ('date_received', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(choices=[('Select bank', 'Select bank'), ('Access Bank', 'Access Bank'), ('Cal Bank', 'Cal Bank'), ('Fidelity Bank', 'Fidelity Bank'), ('Ecobank', 'Ecobank'), ('Adansi rural bank', 'Adansi rural bank'), ('Kwumawuman Bank', 'Kwumawuman Bank'), ('Pan Africa', 'Pan Africa'), ('SGSSB', 'SGSSB'), ('Atwima Rural Bank', 'Atwima Rural Bank'), ('Omnibsic Bank', 'Omnibsic Bank'), ('Omini bank', 'Omini bank'), ('Stanbic Bank', 'Stanbic Bank'), ('First Bank of Nigeria', 'First Bank of Nigeria'), ('Adehyeman Savings and loans', 'Adehyeman Savings and loans'), ('ARB Apex Bank Limited', 'ARB Apex Bank Limited'), ('Absa Bank', 'Absa Bank'), ('Agriculture Development bank', 'Agriculture Development bank'), ('Bank of Africa', 'Bank of Africa'), ('Bank of Ghana', 'Bank of Ghana'), ('Consolidated Bank Ghana', 'Consolidated Bank Ghana'), ('First Atlantic Bank', 'First Atlantic Bank'), ('First National Bank', 'First National Bank'), ('G-Money', 'G-Money'), ('GCB BanK LTD', 'GCB BanK LTD'), ('Ghana Pay', 'Ghana Pay'), ('GHL Bank Ltd', 'GHL Bank Ltd'), ('GT Bank', 'GT Bank'), ('National Investment Bank', 'National Investment Bank'), ('Opportunity International Savings And Loans', 'Opportunity International Savings And Loans'), ('Prudential Bank', 'Prudential Bank'), ('Republic Bank Ltd', 'Republic Bank Ltd'), ('Sahel Sahara Bank', 'Sahel Sahara Bank'), ('Sinapi Aba Savings and Loans', 'Sinapi Aba Savings and Loans'), ('Societe Generale Ghana Ltd', 'Societe Generale Ghana Ltd'), ('Standard Chartered', 'Standard Chartered'), ('universal Merchant Bank', 'universal Merchant Bank'), ('Zenith Bank', 'Zenith Bank'), ('Mtn', 'Mtn'), ('AirtelTigo', 'AirtelTigo'), ('Vodafone', 'Vodafone')], default='Access Bank', max_length=100)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=255)),
                ('created_month', models.CharField(blank=True, default='', max_length=10)),
                ('created_year', models.CharField(blank=True, default='', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
