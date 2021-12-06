from django.db import models
from django.db.models import F
from django.utils.timesince import timeuntil
from datetime import date, timedelta

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    account_name = models.CharField(max_length=200, null=True)
    payment_name = models.CharField(max_length=200, null=True)
    number_of_boxes = models.IntegerField(null=True, default=1)
    server = models.CharField(max_length=200, null=True)
    mac_address = models.CharField(max_length=200, null=True)
    expires = models.DateField(null=True)
    communication = models.CharField(max_length=200, null=True)
    referal = models.CharField(max_length=200, null=True)
    building_type = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    customer_since = models.DateField(null=True)
    notes = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    needs_remind = models.BooleanField(default=False, null=True)

    def __str__(self):
        return str(self.name)

    def expiration(self):
        today = date.today()
        expired = self.expires
        return ((expired - today).days)

    def add_thirty(self):
        self.expires += timedelta(days=30)
        self.save(update_fields=['expires'])

    @property
    def reminder(self):
        if(self.expiration <= 5):
            return True
        return False

