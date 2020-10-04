from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView, RedirectView,
    FormView, View
)
from invoice.models import Invoice
from django.contrib.auth.mixins import LoginRequiredMixin
from invoice.forms import InvoiceCreationForm
from django.shortcuts import redirect
from django.urls import reverse_lazy
from accounts.models import UserProfile
from invoice.tasks import NotifyToManagerForInvoice


class InvoiceListView(LoginRequiredMixin, ListView):
    model = Invoice
    paginate_by = 20
    template_name = 'invoice/invoice_list.html'
    context_object_name = 'invoices'
    login_url = '/'

    def get_queryset(self, *args, **kwargs):
        queryset = super(InvoiceListView, self).get_queryset(
            *args, **kwargs)

        NotifyToManagerForInvoice()
        userprofile = UserProfile.objects.filter(user=self.request.user)
        if not userprofile and userprofile.first().is_manager():
            return queryset.filter(created_by=self.request.user)

        return queryset


class InvoiceCreateView(LoginRequiredMixin, CreateView):
    model = Invoice
    template_name = 'invoice/invoice_create.html'
    form_class = InvoiceCreationForm
    success_url = '/invoice'
    login_url = '/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    context_object_name = 'invoice'
    template_name = 'invoice/invoice_detail.html'
    pk_url_kwarg = 'invoice_id'
