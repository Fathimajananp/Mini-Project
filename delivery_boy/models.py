from django.db import models

# Create your models here.

class DeliveryBoy(models.Model):
    d_id = models.AutoField(primary_key=True)
    log_id = models.IntegerField()
    email_id = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=10)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'delivery_boy'
