from django.db import models

# Create your models here.
class Payment(models.Model):
    p_id = models.AutoField(primary_key=True)
    o_id = models.IntegerField()
    date = models.DateField()
    mode_of_payment = models.CharField(max_length=25)
    amount = models.CharField(max_length=20)
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'payment'
