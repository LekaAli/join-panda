from django.db import models
from django.contrib.auth import settings


class DataTable(models.Model):

    PURCHASE = "purchase"
    SALE = "sale"
    PURCHASE_SALE_OPTIONS = [
        (PURCHASE, "Purchase"),
        (SALE, "Sale")
    ]
    date = models.DateField(blank=True, null=True)
    purchase_or_sale = models.CharField(max_length=15, choices=PURCHASE_SALE_OPTIONS, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    currency = models.CharField(max_length=5, blank=True, null=True)
    net = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)

