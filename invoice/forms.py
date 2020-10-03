from django import forms
from invoice.models import Invoice, Item


class InvoiceCreationForm(forms.ModelForm):

    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all())
    class Meta:
        model = Invoice
        fields = ['vendor_name', 'attachment', 'items']
