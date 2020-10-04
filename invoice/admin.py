from django.contrib import admin
from invoice.models import *
# Register your models here.

admin.site.register(Invoice)
admin.site.register(Item)
admin.site.register(RawItem)
