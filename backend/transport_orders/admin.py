from django.contrib import admin
from .models import TransportOrder
from waypoints.models import Waypoint


class WaypointInline(admin.TabularInline):
    model = Waypoint
    extra = 1


class TransportOrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'date', 'date_created')
    inlines = [WaypointInline]


admin.site.register(TransportOrder, TransportOrderAdmin)

