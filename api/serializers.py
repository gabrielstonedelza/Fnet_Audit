from rest_framework import serializers
from .models import Company, AddCompanyAmountReceived, AddCompanyAmountPayment

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','agent','bank','name','phone','account_number','date_created','get_agent_username','created_month','created_year','company_whatsapp_phone','email']
        read_only_fields = ['agent']

class AddCompanyAmountReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCompanyAmountReceived
        fields = ['id','agent','company','amount_received','receipt','unique_identifier','date_received','get_agent_username','get_receipt_pic','account_number','received_month','received_year']
        read_only_fields = ['agent']

class AddCompanyAmountPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCompanyAmountPayment
        fields = ['id','agent','company','amount','screenshot','unique_identifier','date_paid','get_agent_username','get_screenshot_pic','get_company_amount_received','get_amount_received_receipt','get_amount_received_date','get_company_name','get_account_number','payment_month','payment_year','get_company_phone','get_company_whatsapp_phone','company_amount']
        read_only_fields = ['agent']
