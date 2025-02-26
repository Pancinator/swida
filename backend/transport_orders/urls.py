from django.urls import path

from .serializers.serializers import TransportOrderSerializer
from .services.services import TransportOrderService
from .views import CreateOrderView, ListOrdersView

urlpatterns = [
    path('orders/', ListOrdersView.as_view(
        serializer_class=TransportOrderSerializer,
        order_service=TransportOrderService()
    ), name='orders-list'),
    path('orders/create/', CreateOrderView.as_view(
        serializer_class=TransportOrderSerializer,
        order_service=TransportOrderService()
    ), name='orders-create'),
]
