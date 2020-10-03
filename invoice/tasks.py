from celery.decorators import task
import datetime
from invoice.models import Invoice
from accounts.models import UserProfile


@task()
def test():
    print("working")

# @task()


def NotifyToManagerForInvoice():

    managers = UserProfile.objects.filter(user_type='manager')
    context_dict = {}
    print("working!!!!!!")

    for manager in managers:
        agents = manager.agents.all()
        invoices = Invoice.objects.filter(
            created_by__id__in=agents)
        context_dict['manager_name'] = manager.get_full_name()

        context_dict['number_of_invoices'] = invoices.values_list(
            'user__id', flat=True).count()
        context_dict['total_amount'] = invoices.aggregate(Sum('price'))
