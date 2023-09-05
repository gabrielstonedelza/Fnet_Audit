import random
from datetime import datetime

from PIL import Image
from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

BANKS = (
    ("Select bank", "Select bank"),
    ("Access Bank", "Access Bank"),
    ("Cal Bank", "Cal Bank"),
    ("Fidelity Bank", "Fidelity Bank"),
    ("Ecobank", "Ecobank"),
    ("Adansi rural bank", "Adansi rural bank"),
    ("Kwumawuman Bank", "Kwumawuman Bank"),
    ("Pan Africa", "Pan Africa"),
    ("SGSSB", "SGSSB"),
    ("Atwima Rural Bank", "Atwima Rural Bank"),
    ("Omnibsic Bank", "Omnibsic Bank"),
    ("Omini bank", "Omini bank"),
    ("Stanbic Bank", "Stanbic Bank"),
    ("First Bank of Nigeria", "First Bank of Nigeria"),
    ("Adehyeman Savings and loans", "Adehyeman Savings and loans",),
    ("ARB Apex Bank Limited", "ARB Apex Bank Limited",),
    ("Absa Bank", "Absa Bank"),
    ("Agriculture Development bank", "Agriculture Development bank"),
    ("Bank of Africa", "Bank of Africa"),
    ("Bank of Ghana", "Bank of Ghana"),
    ("Consolidated Bank Ghana", "Consolidated Bank Ghana"),
    ("First Atlantic Bank", "First Atlantic Bank"),
    ("First National Bank", "First National Bank"),
    ("G-Money", "G-Money"),
    ("GCB BanK LTD", "GCB BanK LTD"),
    ("Ghana Pay", "Ghana Pay"),
    ("GHL Bank Ltd", "GHL Bank Ltd"),
    ("GT Bank", "GT Bank"),
    ("National Investment Bank", "National Investment Bank"),
    ("Opportunity International Savings And Loans", "Opportunity International Savings And Loans"),
    ("Prudential Bank", "Prudential Bank"),
    ("Republic Bank Ltd", "Republic Bank Ltd"),
    ("Sahel Sahara Bank", "Sahel Sahara Bank"),
    ("Sinapi Aba Savings and Loans", "Sinapi Aba Savings and Loans"),
    ("Societe Generale Ghana Ltd", "Societe Generale Ghana Ltd"),
    ("Standard Chartered", "Standard Chartered"),
    ("universal Merchant Bank", "universal Merchant Bank"),
    ("Zenith Bank", "Zenith Bank"),
    ("Mtn", "Mtn"),
    ("AirtelTigo", "AirtelTigo"),
    ("Vodafone", "Vodafone"),
)

AMOUNT_RECEIVED_PAID_STATUS = (
    ("Pending", "Pending"),
    ("Paid", "Paid"),
)


class Company(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS, default="Access Bank")
    email = models.EmailField(max_length=255, unique=True, default='')
    name = models.CharField(max_length=255, blank=True)
    company_whatsapp_phone = models.CharField(max_length=15, default="", blank=True)
    phone = models.CharField(max_length=20, blank=True)
    account_number = models.CharField(max_length=255, blank=True)
    created_month = models.CharField(max_length=10, blank=True, default="")
    created_year = models.CharField(max_length=10, blank=True, default="")
    date_created = models.DateTimeField(auto_now_add=True)

    def get_agent_username(self):
        return self.agent.username

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.created_month = de_date.month
        self.created_year = de_date.year
        super().save(*args, **kwargs)


class AddCompanyAmountReceived(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount_received = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    receipt = models.ImageField(upload_to="receipts", default="receipt.png", blank=True)
    unique_identifier = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=255, blank=True)
    amount_received_paid = models.CharField(max_length=30, choices=AMOUNT_RECEIVED_PAID_STATUS, default="Pending")
    received_month = models.CharField(max_length=10, blank=True, default="")
    received_year = models.CharField(max_length=10, blank=True, default="")
    transaction_id = models.CharField(max_length=255, default="", blank=True)
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name

    def get_agent_username(self):
        return self.agent.username

    def get_company_name(self):
        return self.company.name

    def get_company_email(self):
        return self.company.email

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.received_month = de_date.month
        self.received_year = de_date.year
        self.unique_identifier = self.company.name[:5] + str(random.randint(1, 90000))
        self.account_number = self.company.account_number
        super().save(*args, **kwargs)

        img = Image.open(self.receipt.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.receipt.path)

    def get_receipt_pic(self):
        if self.receipt:
            return "https://agencybankingnetwork.com" + self.receipt.url
        return ''


class AddCompanyAmountPayment(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    company_amount = models.ForeignKey(AddCompanyAmountReceived, on_delete=models.CASCADE,
                                       related_name='company_amount')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount1 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount2 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount3 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount4 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount5 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount6 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount7 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount8 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount9 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount10 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount11 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount12 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount13 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount14 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount15 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount16 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount17 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount18 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount19 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    amount20 = models.DecimalField(max_digits=19, decimal_places=2, blank=True, default=0.0)
    screenshot = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot1 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot2 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot3 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot4 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot5 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot6 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot7 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot8 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot9 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot10 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot11 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot12 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot13 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot14 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot15 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot16 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot17 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot18 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot19 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    screenshot20 = models.ImageField(upload_to="screenshots", default="screenshot.png")
    unique_identifier = models.CharField(max_length=255, blank=True)
    payment_month = models.CharField(max_length=10, blank=True, default="")
    payment_year = models.CharField(max_length=10, blank=True, default="")
    transaction_id = models.CharField(max_length=255, default="")
    transaction_id1 = models.CharField(max_length=255, default="")
    transaction_id2 = models.CharField(max_length=255, default="")
    transaction_id3 = models.CharField(max_length=255, default="")
    transaction_id4 = models.CharField(max_length=255, default="")
    transaction_id5 = models.CharField(max_length=255, default="")
    transaction_id6 = models.CharField(max_length=255, default="")
    transaction_id7 = models.CharField(max_length=255, default="")
    transaction_id8 = models.CharField(max_length=255, default="")
    transaction_id9 = models.CharField(max_length=255, default="")
    transaction_id10 = models.CharField(max_length=255, default="")
    transaction_id11 = models.CharField(max_length=255, default="")
    transaction_id12 = models.CharField(max_length=255, default="")
    transaction_id13 = models.CharField(max_length=255, default="")
    transaction_id14 = models.CharField(max_length=255, default="")
    transaction_id15 = models.CharField(max_length=255, default="")
    transaction_id16 = models.CharField(max_length=255, default="")
    transaction_id17 = models.CharField(max_length=255, default="")
    transaction_id18 = models.CharField(max_length=255, default="")
    transaction_id19 = models.CharField(max_length=255, default="")
    transaction_id20 = models.CharField(max_length=255, default="")
    date_paid = models.DateTimeField(auto_now_add=True)

    def get_agent_username(self):
        return self.agent.username

    def __str__(self):
        return self.company.name

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.payment_month = de_date.month
        self.payment_year = de_date.year
        self.unique_identifier = self.company_amount.unique_identifier
        super().save(*args, **kwargs)

        img = Image.open(self.screenshot.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.screenshot.path)

    def get_screenshot_pic(self):
        if self.screenshot:
            return "https://agencybankingnetwork.com" + self.screenshot.url
        return ''

    def get_company_amount_received(self):
        return self.company_amount.amount_received

    def get_amount_received_receipt(self):
        if self.company_amount.receipt:
            return "https://agencybankingnetwork.com" + self.company_amount.receipt.url
        return ''

    def get_amount_received_date(self):
        return self.company_amount.date_received

    def get_company_name(self):
        return self.company.name

    def get_account_number(self):
        return self.company.account_number

    def get_company_phone(self):
        return self.company.phone

    def get_company_whatsapp_phone(self):
        return self.company.company_whatsapp_phone

    def get_company_email(self):
        return self.company.email

    def get_transaction_id(self):
        return self.company_amount.transaction_id
