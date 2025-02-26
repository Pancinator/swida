from rest_framework import serializers

from waypoints.models import Waypoint
from transport_orders.models import TransportOrder


class WaypointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waypoint
        fields = ['uuid', 'location', 'waypoint_type']


class TransportOrderSerializer(serializers.ModelSerializer):
    waypoints = WaypointSerializer(many=True)

    class Meta:
        model = TransportOrder
        fields = ['uuid', 'order_number', 'customer_name', 'date', 'waypoints']
