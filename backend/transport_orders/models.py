from django.db import models
from myproject.base_model import BaseModel


class Order(BaseModel):
    class Meta:
        abstract = True


class TransportOrder(Order):
    objects = models.Manager()
    order_number = models.CharField(max_length=100)
    customer_name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return f"{self.order_number} - {self.customer_name}"
