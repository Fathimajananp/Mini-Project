from django.db import models

# Create your models here.
class ItemDetails(models.Model):
    item_id = models.AutoField(primary_key=True)
    m_id = models.IntegerField()
    image = models.TextField()
    status = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'item_details'
