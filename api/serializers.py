from rest_framework import serializers

from .models import Company, AddCompanyAmountReceived, AddCompanyAmountPayment


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'agent', 'bank', 'name', 'phone', 'account_number', 'date_created', 'get_agent_username',
                  'created_month', 'created_year', 'company_whatsapp_phone', 'email']
        read_only_fields = ['agent']


class AddCompanyAmountReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCompanyAmountReceived
        fields = ['id', 'agent', 'company', 'amount_received', 'receipt', 'unique_identifier', 'date_received',
                  'get_agent_username', 'get_receipt_pic', 'account_number', 'received_month', 'received_year',
                  'get_company_name', 'get_company_email', 'transaction_id', 'amount_received_paid', 'd_200', 'd_100',
                  'd_50',
                  'd_20', 'd_10', 'd_5', 'd_2', 'd_1', 'teller_name', 'teller_phone']
        read_only_fields = ['agent']


class AddCompanyAmountPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddCompanyAmountPayment
        fields = ['id', 'agent', 'company', 'amount', 'screenshot', 'unique_identifier', 'date_paid',
                  'get_agent_username', 'get_screenshot_pic', 'get_company_amount_received',
                  'get_amount_received_receipt', 'get_amount_received_date', 'get_company_name', 'get_account_number',
                  'payment_month', 'payment_year', 'get_company_phone', 'get_company_whatsapp_phone', 'company_amount',
                  'get_company_amount_received_username',
                  'transaction_id', 'get_transaction_id',
                  'amount1',
                  'amount2',
                  'amount3',
                  'amount4',
                  'amount5',
                  'amount6',
                  'amount7',
                  'amount8',
                  'amount9',
                  'amount10',
                  'amount11',
                  'amount12',
                  'amount13',
                  'amount14',
                  'amount15',
                  'amount16',
                  'amount17',
                  'amount18',
                  'amount19',
                  'amount20',
                  'screenshot1',
                  'screenshot2',
                  'screenshot3',
                  'screenshot4',
                  'screenshot5',
                  'screenshot6',
                  'screenshot7',
                  'screenshot8',
                  'screenshot9',
                  'screenshot10',
                  'screenshot11',
                  'screenshot12',
                  'screenshot13',
                  'screenshot14',
                  'screenshot15',
                  'screenshot16',
                  'screenshot17',
                  'screenshot18',
                  'screenshot19',
                  'screenshot20',
                  'transaction_id1',
                  'transaction_id2',
                  'transaction_id3',
                  'transaction_id4',
                  'transaction_id5',
                  'transaction_id6',
                  'transaction_id7',
                  'transaction_id8',
                  'transaction_id9',
                  'transaction_id10',
                  'transaction_id11',
                  'transaction_id12',
                  'transaction_id13',
                  'transaction_id14',
                  'transaction_id15',
                  'transaction_id16',
                  'transaction_id17',
                  'transaction_id18',
                  'transaction_id19',
                  'transaction_id20',
                  'get_screenshot_pic1',
                  'get_screenshot_pic2',
                  'get_screenshot_pic3',
                  'get_screenshot_pic4',
                  'get_screenshot_pic5',
                  'get_screenshot_pic6',
                  'get_screenshot_pic7',
                  'get_screenshot_pic8',
                  'get_screenshot_pic9',
                  'get_screenshot_pic10',
                  'get_screenshot_pic11',
                  'get_screenshot_pic12',
                  'get_screenshot_pic13',
                  'get_screenshot_pic14',
                  'get_screenshot_pic15',
                  'get_screenshot_pic16',
                  'get_screenshot_pic17',
                  'get_screenshot_pic18',
                  'get_screenshot_pic19',
                  'get_screenshot_pic20',
                  'get_company_amount_received_teller_name',
                  'get_company_amount_received_teller_phone'
                  ]
        read_only_fields = ['agent']
