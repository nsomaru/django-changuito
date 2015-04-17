# -*- coding: utf-8 -*-
from django.contrib import admin

import reversion

from .models import Order 

# Admin actions
def cancel(modeladmin, request, queryset):
    rows_updated = [q.cancel() for q in queryset]
    if len(rows_updated) == 1:
        message_bit = "1 order was"
    else:
        message_bit = "%s orders were" % len(rows_updated)
    modeladmin.message_user(request, "%s sucessfully marked as cancelled")
    
def invalidate(modeladmin, request, queryset):
    rows_updated = [q.invalidate() for q in queryset]
    if len(rows_updated) == 1:
        message_bit = "1 order was"
    else:
        message_bit = "%s orders were" % len(rows_updated)
    modeladmin.message_user(request, "%s sucessfully marked as invalid")

def confirm(modeladmin, request, queryset):
    rows_updated = [q.confirm() for q in queryset]
    if len(rows_updated) == 1:
        message_bit = "1 order was"
    else:
        message_bit = "%s orders were" % len(rows_updated)
    modeladmin.message_user(request, "%s sucessfully marked as confirmed")

cancel.short_description = "Mark selected as cancelled"
invalidate.short_description = "Mark selected as invalid"
confirm.short_description = "Mark selected as confirmed"


class OrderAdmin(reversion.VersionAdmin):
    fields = ('customer_name', 'email', 'shipping_address')
    list_display = ('number', 'date_created', 'customer_name', 'email', 'slug')

admin.site.register(Order, OrderAdmin)
