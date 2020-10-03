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
    import pdb
    pdb.set_trace()
    for manager in managers:
        context_dict['manager_name'] = manager.get_full_name()
        context_dict['number_of_invoices'] = Invoice.objects.filter(
            created_by__id__in=manager.agents.all().values_list('user__id', flat=True)).count()

        