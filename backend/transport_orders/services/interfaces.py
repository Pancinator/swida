from abc import ABC, abstractmethod

from django.http import QueryDict

from transport_orders.models import Order


class IOrderService(ABC):
    @abstractmethod
    def create_order(self, validated_data):
        """
        Creates order based on validated data
        """
        pass

    def get_orders(self, query_params: QueryDict):
        """
        Get list of orders based on query params, if query_params are not provided, return all orders
        :param query_params:
        :return:
        """
        pass

    def get_order_by_uuid(self, uuid: str):
        """
        Get order by uuid
        :param uuid:
        :return:
        """
        pass

    def delete_order(self, order: Order):
        """
        Delete order
        :param order:
        :return:
        """
        pass
