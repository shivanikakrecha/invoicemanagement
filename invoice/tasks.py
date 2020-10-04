from celery.decorators import task
from datetime import datetime, timedelta
from invoice.models import Invoice
from accounts.models import UserProfile
from django.db.models import Sum
from invoice.utils import SendEmailToUsers


@task()
def test():
    print("working")

# @task()


def NotifyToManagerForInvoice():

    managers = UserProfile.objects.filter(user_type='manager')
    context_dict = {}

    today = datetime.now()
    yesterday = datetime.strftime((today - timedelta(1)), "%Y-%m-%d")

    for manager in managers:
        agents = manager.agents.all()
        invoices = Invoice.objects.filter(
            created_by__id__in=agents)
        context_dict['manager_name'] = manager.get_full_name()
        context_dict['previous_day'] = yesterday
        context_dict['number_of_invoices'] = invoices.values_list(
            'created_by__id', flat=True).count()

        total_amount = 0

        for invoice in invoices:
            total_amount += invoice.items.all().aggregate(Sum('price')
                                                          )['price__sum']

            context_dict['pdf'] = invoice.attachment

        context_dict['total_amount'] = total_amount
        SendEmailToUsers(context_dict, manager.user.email)
