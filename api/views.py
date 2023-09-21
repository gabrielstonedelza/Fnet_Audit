from django.conf import settings
from django.core.mail import EmailMessage
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import filters
from rest_framework import permissions, generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from users.models import User
from .models import Company, AddCompanyAmountReceived, AddCompanyAmountPayment
from .serializers import CompanySerializer, AddCompanyAmountReceivedSerializer, AddCompanyAmountPaymentSerializer


# company
# register company
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_new_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_company(request, pk):
    account = get_object_or_404(Company, pk=pk)
    serializer = CompanySerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_company(request, pk):
    try:
        owner_bank_accounts = get_object_or_404(Company, pk=pk)
        owner_bank_accounts.delete()
    except Company.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_my_companies(request):
    companies = Company.objects.filter(agent=request.user).order_by('-date_created')
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_companies(request):
    companies = Company.objects.all().order_by('-date_created')
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


class SearchCompany(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Company.objects.all().order_by('-date_created')
    serializer_class = CompanySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'phone']


# add company amount received
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_new_company_amount_received(request, com_email):
    serializer = AddCompanyAmountReceivedSerializer(data=request.data)
    if serializer.is_valid():
        amount_received = serializer.save(agent=request.user)
        # Send an email with the amount_received details and screenshot
        subject = 'Amount Details'
        message = f"An amount of ${amount_received.amount_received} has been received from {amount_received.agent.username}."
        from_email = settings.EMAIL_HOST_USER
        to_email = [com_email, "fnetbankghana@gmail.com"]  # Assuming user provides email in the request

        email = EmailMessage(subject, message, from_email, to_email)
        email.attach_file(amount_received.receipt.path)
        email.send()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_company_amount_received(request, pk):
    account = get_object_or_404(AddCompanyAmountReceived, pk=pk)
    serializer = AddCompanyAmountReceivedSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_company_amount_received(request, pk):
    try:
        owner_bank_accounts = get_object_or_404(AddCompanyAmountReceived, pk=pk)
        owner_bank_accounts.delete()
    except AddCompanyAmountReceived.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_companies_amount_received_not_paid(request):
    companies = AddCompanyAmountReceived.objects.filter(agent=request.user).filter(
        amount_received_paid="Pending").order_by('-date_received')
    serializer = AddCompanyAmountReceivedSerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_companies_amount_received_paid(request):
    companies = AddCompanyAmountReceived.objects.filter(agent=request.user).filter(
        amount_received_paid="Paid").order_by('-date_received')
    serializer = AddCompanyAmountReceivedSerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_companies_amount_received(request):
    companies = AddCompanyAmountReceived.objects.all().order_by('-date_received')
    serializer = AddCompanyAmountReceivedSerializer(companies, many=True)
    return Response(serializer.data)


class SearchCompanyAmountReceived(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AddCompanyAmountReceived.objects.all().order_by('-date_received')
    serializer_class = AddCompanyAmountReceivedSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['account_number', 'date_received']


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def search_my_company_amount_received_by_date(request, d_month, d_year):
    company = AddCompanyAmountReceived.objects.filter(agent=request.user).filter(received_month=d_month).filter(
        received_year=d_year).order_by("-date_received")
    serializer = AddCompanyAmountReceivedSerializer(company, many=True)
    return Response(serializer.data)


# company payments

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_new_company_payment(request, com_email):
    serializer = AddCompanyAmountPaymentSerializer(data=request.data)
    if serializer.is_valid():
        payment = serializer.save(agent=request.user)
        # Send an email with the payment details and screenshot
        subject = 'Payment Details'
        message = f"Payment of ${payment.amount} has been received from {payment.agent.username}."
        from_email = settings.EMAIL_HOST_USER
        to_email = [com_email, "fnetbankghana@gmail.com"]  # Assuming user provides email in the request

        email = EmailMessage(subject, message, from_email, to_email)
        email.attach_file(payment.screenshot.path)
        email.send()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_company_payment(request, pk):
    account = get_object_or_404(AddCompanyAmountPayment, pk=pk)
    serializer = AddCompanyAmountPaymentSerializer(account, data=request.data)
    if serializer.is_valid():
        serializer.save(agent=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_company_payment(request, pk):
    try:
        owner_bank_accounts = get_object_or_404(AddCompanyAmountPayment, pk=pk)
        owner_bank_accounts.delete()
    except AddCompanyAmountPayment.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_companies_payments(request):
    companies = AddCompanyAmountPayment.objects.filter(agent=request.user).order_by('-date_paid')
    serializer = AddCompanyAmountPaymentSerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_companies_payments(request):
    companies = AddCompanyAmountPayment.objects.all().order_by('-date_paid')
    serializer = AddCompanyAmountPaymentSerializer(companies, many=True)
    return Response(serializer.data)


class SearchCompanyPayments(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = AddCompanyAmountPayment.objects.all().order_by('-date_paid')
    serializer_class = AddCompanyAmountPaymentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['unique_identifier', 'date_paid']


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def search_my_company_payment_by_date(request, d_month, d_year):
    company = AddCompanyAmountPayment.objects.filter(agent=request.user).filter(payment_month=d_month).filter(
        payment_year=d_year).order_by("-date_paid")
    serializer = AddCompanyAmountPaymentSerializer(company, many=True)
    return Response(serializer.data)


# for admin purposes
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_agents_companies(request, username):
    user = get_object_or_404(User, username=username)
    companies = Company.objects.filter(agent=user).order_by('-date_created')
    serializer = CompanySerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_agents_companies_amount_received(request, username):
    user = get_object_or_404(User, username=username)
    companies = AddCompanyAmountReceived.objects.filter(agent=user).order_by('-date_received')
    serializer = AddCompanyAmountReceivedSerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_agents_companies_payments(request, username):
    user = get_object_or_404(User, username=username)
    companies = AddCompanyAmountPayment.objects.filter(agent=user).order_by('-date_paid')
    serializer = AddCompanyAmountPaymentSerializer(companies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search_agents_company_payment_by_date(request, username, d_month, d_year):
    user = get_object_or_404(User, username=username)
    company = AddCompanyAmountPayment.objects.filter(agent=user).filter(payment_month=d_month).filter(
        payment_year=d_year).order_by("-date_paid")
    serializer = AddCompanyAmountPaymentSerializer(company, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def search_agents_company_amount_received_by_date(request, username, d_month, d_year):
    user = get_object_or_404(User, username=username)
    company = AddCompanyAmountReceived.objects.filter(agent=user).filter(received_month=d_month).filter(
        received_year=d_year).order_by("-date_received")
    serializer = AddCompanyAmountReceivedSerializer(company, many=True)
    return Response(serializer.data)


# get company by name
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_company_by_name(request, name):
    company = Company.objects.filter(name=name)
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_company_by_id(request, id):
    company = get_object_or_404(AddCompanyAmountReceived, id=id)
    serializer = AddCompanyAmountReceivedSerializer(company, many=False)
    return Response(serializer.data)


# customer

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_company_details(request, company):
    company = Company.objects.filter(name=company).order_by("-date_created")
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customer_company_amounts_received(request, company):
    company_amounts_received = AddCompanyAmountReceived.objects.filter(company=company).order_by("-date_received")
    serializer = AddCompanyAmountReceivedSerializer(company_amounts_received, many=True)
    return Response(serializer.data)
