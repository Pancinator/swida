from django.db import models

from myproject.base_model import BaseModel
from transport_orders.models import TransportOrder


class Waypoint(BaseModel):
    objects = models.Manager()
    PICKUP = 'Pickup'
    DELIVERY = 'Delivery'
    WAYPOINT_CHOICES = [
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
    ]

    transport_order = models.ForeignKey(TransportOrder, related_name='waypoints', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    waypoint_type = models.CharField(max_length=10, choices=WAYPOINT_CHOICES)

    def __str__(self):
        return f"{self.waypoint_type} - {self.location}"

