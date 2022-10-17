from django.db import models
from user.models import User
from Meat.models import Meats
# Create your models here.

class OrderDetails(models.Model):
    o_id = models.AutoField(primary_key=True)
    c=models.ForeignKey(User,to_field="c_id",on_delete=models.CASCADE)
    # c_id = models.IntegerField()
    # m_id = models.IntegerField()
    m=models.ForeignKey(Meats,to_field="m_id",on_delete=models.CASCADE)

    date = models.DateField()
    delivery_date = models.DateField()
    status = models.CharField(max_length=30)
    choosen_quantity = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'order_details'
