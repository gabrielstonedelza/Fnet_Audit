from django.urls import path
from . import views

urlpatterns = [
    #  company
    path("add_new_company/", views.add_new_company),
    path("update_company/<int:pk>/", views.update_company),
    path("delete_company/<int:pk>/", views.delete_company),
    path("get_my_companies/", views.get_my_companies),
    path("get_all_companies/", views.get_all_companies),
    path("search_companies/", views.SearchCompany.as_view()),

#     amount received
    path("add_new_company_amount_received/<str:com_email>/", views.add_new_company_amount_received),
    path("update_company_amount_received/<int:pk>/", views.update_company_amount_received),
    path("delete_company_amount_received/<int:pk>/", views.delete_company_amount_received),
    path("get_my_companies_amount_received/", views.get_my_companies_amount_received),
    path("get_all_companies_amount_received/", views.get_all_companies_amount_received),
    path("search_companies_amount_received/", views.SearchCompanyAmountReceived.as_view()),
    path("search_my_company_amount_received_by_date/<str:d_month>/<str:d_year>/", views.search_my_company_amount_received_by_date),

#     payments
    path("add_new_company_payment/<str:com_email>/", views.add_new_company_payment),
    path("update_company_payment/<int:pk>/", views.update_company_payment),
    path("delete_company_payment/<int:pk>/", views.delete_company_payment),
    path("get_my_companies_payments/", views.get_my_companies_payments),
    path("get_all_companies_payments/", views.get_all_companies_payments),
    path("search_companies_payments/", views.SearchCompanyPayments.as_view()),
    path("search_my_company_payment_by_date/<str:d_month>/<str:d_year>/", views.search_my_company_amount_received_by_date),
    path("get_company_by_name/<str:name>/",views.get_company_by_name),
    path("get_company_payment_by_name/<str:company_amount>/",views.get_company_by_name),


#     admin
    path("get_agents_companies/", views.get_agents_companies),
    path("get_agents_companies_amount_received/", views.get_agents_companies_amount_received),
    path("get_agents_companies_payments/", views.get_agents_companies_payments),
    path("search_agents_company_payment_by_date/", views.search_agents_company_payment_by_date),
    path("search_agents_company_amount_received_by_date/", views.search_agents_company_amount_received_by_date),

]