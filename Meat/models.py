from django.db import models

# Create your models here.


class Meats(models.Model):
    m_id = models.AutoField(primary_key=True)
    meat_name = models.CharField(max_length=30)
    items = models.CharField(max_length=25)
    type = models.CharField(max_length=20)
    quantity = models.CharField(max_length=50)
    price_kg = models.CharField(db_column='price/kg', max_length=50)  # Field renamed to remove unsuitable characters.
    image = models.CharField(max_length=50)
    status = models.CharField(max_length=30)
    date_meat = models.DateField()

    class Meta:
        managed = False
        db_table = 'Meats'





