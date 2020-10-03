from django.urls import path, include
from invoice.views import InvoiceListView, InvoiceCreateView, InvoiceDetailView
from invoice.tasks import NotifyToManagerForInvoice

app_name = 'invoice'

urlpatterns = [
    path('', InvoiceListView.as_view(), name='invoice_list'),
    path('create-invoice', InvoiceCreateView.as_view(), name='invoice_create'),
    path('detail-invoice/<int:invoice_id>',
         InvoiceDetailView.as_view(), name='invoice_detail')
]
