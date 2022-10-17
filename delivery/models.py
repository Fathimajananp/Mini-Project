from django.db import models

# Create your models here.
class Delivery(models.Model):
    a_id = models.AutoField(primary_key=True)
    d_id = models.IntegerField()
    o_id = models.IntegerField()
    time = models.TimeField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'delivery'
