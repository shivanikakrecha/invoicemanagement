from django.db.models.signals import pre_save
from invoice.models import Item


def CalculatePriceCost(sender, instance, **kwargs):
    instance.price = instance.raw_item.price * instance.quantity


pre_save.connect(CalculatePriceCost, sender=Item)
