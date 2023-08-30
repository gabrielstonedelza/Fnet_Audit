from django.contrib import admin
from .models import Company, AddCompanyAmountReceived, AddCompanyAmountPayment

admin.site.register(Company)
admin.site.register(AddCompanyAmountReceived)
admin.site.register(AddCompanyAmountPayment)
