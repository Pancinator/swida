from typing import Type

from rest_framework.serializers import ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from transport_orders.serializers.serializers import TransportOrderSerializer
from transport_orders.services.interfaces import IOrderService
from transport_orders.services.services import TransportOrderService


class CreateOrderView(APIView):
    """
    Default values provded because of swagger docs
    """
    serializer_class: Type[ModelSerializer] = TransportOrderSerializer
    order_service: IOrderService = TransportOrderService

    def __init__(self, serializer_class: Type[ModelSerializer] = TransportOrderSerializer,
                 order_service: IOrderService = TransportOrderService, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = serializer_class
        self.order_service = order_service

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            order = self.order_service.create_order(serializer.validated_data)
            output_serializer = self.serializer_class(order)

            return Response(output_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListOrdersView(generics.ListAPIView):
    serializer_class: Type[ModelSerializer] = None
    order_service: IOrderService = None

    def __init__(self, serializer_class: Type[ModelSerializer] = TransportOrderSerializer,
                 order_service: IOrderService = TransportOrderService, **kwargs):
        super().__init__(**kwargs)
        self.serializer_class = serializer_class
        self.order_service = order_service

    def get_serializer_class(self):
        return self.serializer_class

    def get_queryset(self):
        return self.order_service.get_orders(self.request.query_params)


class DeleteOrderView(APIView):
    order_service: IOrderService = TransportOrderService

    def __init__(self, order_service: IOrderService = TransportOrderService, **kwargs):
        super().__init__(**kwargs)
        self.order_service = order_service

    def delete(self, uuid):
        order = self.order_service.get_order_by_uuid(uuid)
        if not order:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        self.order_service.delete_order(order)
        return Response(status=status.HTTP_204_NO_CONTENT)
