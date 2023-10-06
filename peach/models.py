from django.db import models
from django.utils.translation import gettext_lazy as _


class Item(models.Model):
    name = models.CharField(unique=True, max_length=64, verbose_name=_("name"))
    number_of_inventory = models.PositiveIntegerField(default=0, verbose_name=_("number of inventory"))
    price = models.FloatField(verbose_name=_("price"))
    first_record_date = models.DateTimeField(auto_now_add=True, verbose_name=_("first record date"))
    last_charge_date = models.DateTimeField(auto_now_add=True, verbose_name=_("last charge date"))
    description = models.TextField(blank=True, null=True, verbose_name=_("description"))