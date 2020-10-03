from django.db import models
from accounts.models import UserProfile
from invoice.validators import validate_file_attachment
from django.contrib.auth.models import User


# Create your models here.


class TimeStamps(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Item(TimeStamps, models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Invoice(TimeStamps, models.Model):
    invoice_number = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='invoice_created_by')
    vendor_name = models.CharField(max_length=40)
    attachment = models.FileField(upload_to='documents/', null=True, blank=True,
                                  validators=[validate_file_attachment, ])
    items = models.ManyToManyField(Item, null=True, blank=True)

    def __unicode__(self):
        return self.invoice_number

    def save(self, **kwargs):
        self.invoice_number = "IN-"+str(self.id)
        super(Invoice, self).save()
