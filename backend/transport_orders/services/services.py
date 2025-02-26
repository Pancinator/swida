from typing import Any

from django.db.models import QuerySet

from transport_orders.models import TransportOrder, Order
from transport_orders.services.interfaces import IOrderService
from waypoints.models import Waypoint


class TransportOrderService(IOrderService):
    """
    Service layer is present because of the possibilty to have another business logic here in the future
    """

    def create_order(self, validated_data) -> Order:
        waypoints_data = validated_data.pop('waypoints', [])
        order = TransportOrder.objects.create(**validated_data)

        for waypoint_data in waypoints_data:
            Waypoint.objects.create(transport_order=order, **waypoint_data)
        return order

    def get_orders(self, query_params) -> QuerySet[Order]:
        queryset = TransportOrder.objects.all()
        customer_name = query_params.get('customer_name')
        order_date = query_params.get('date')
        if customer_name:
            queryset = queryset.filter(customer_name__icontains=customer_name)
        if order_date:
            queryset = queryset.filter(date=order_date)
        return queryset

    def get_order_by_uuid(self, order_uuid: str) -> Any | None:
        try:
            return TransportOrder.objects.get(uuid=order_uuid)
        except TransportOrder.DoesNotExist:
            return None

    def delete_order(self, order) -> None:
        order.delete()

