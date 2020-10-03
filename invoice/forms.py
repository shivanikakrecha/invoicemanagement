from django import forms
from invoice.models import Invoice


class InvoiceCreationForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['vendor_name', 'attachment']
