from django.db.models.signals import pre_save, post_save
from invoice.models import Item, Invoice


def CalculatePriceCost(sender, instance, **kwargs):
    instance.price = instance.raw_item.price * instance.quantity


pre_save.connect(CalculatePriceCost, sender=Item)


def AssignUserAndCreateInvoiceID(sender, instance, created, **kwargs):
    if created:
        instance.invoice_number = "IN-"+str(instance.id)
        instance.save()


post_save.connect(AssignUserAndCreateInvoiceID, sender=Invoice)
