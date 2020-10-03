from django.urls import path, include
from invoice.views import InvoiceListView, InvoiceCreateView
from invoice.tasks import NotifyToManagerForInvoice

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('create-invoice', InvoiceCreateView.as_view(), name='invoice_create'),
]
