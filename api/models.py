from django.db import models
from django.conf import settings
from PIL import Image
import random
from datetime import datetime


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
class Company(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS, default="Access Bank")
    email = models.EmailField(max_length=255, unique=True, default='')
    name = models.CharField(max_length=255,blank=True)
    company_whatsapp_phone = models.CharField(max_length=15, default="",blank=True)
    phone = models.CharField(max_length=20,blank=True)
    account_number = models.CharField(max_length=255,blank=True)
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
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    amount_received = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    receipt = models.ImageField(upload_to="receipts", default="receipt.png")
    unique_identifier = models.CharField(max_length=255,blank=True)
    account_number = models.CharField(max_length=255,blank=True)
    received_month = models.CharField(max_length=10, blank=True, default="")
    received_year = models.CharField(max_length=10, blank=True, default="")
    date_received = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company.name

    def get_agent_username(self):
        return self.agent.username

    def get_company_name(self):
        return self.company.name

    def save(self, *args, **kwargs):
        my_date = datetime.today()
        de_date = my_date.date()
        self.received_month = de_date.month
        self.received_year = de_date.year
        self.unique_identifier = self.company.name[:5] + str(random.randint(1,90000))
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
    company_amount = models.ForeignKey(AddCompanyAmountReceived,on_delete=models.CASCADE,related_name='company_amount',default=1)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True)
    screenshot = models.ImageField(upload_to="screenshots", default="screenshot.png")
    unique_identifier = models.CharField(max_length=255,blank=True)
    payment_month = models.CharField(max_length=10, blank=True, default="")
    payment_year = models.CharField(max_length=10, blank=True, default="")
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
