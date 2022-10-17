from django.db import models

# Create your models here.
class User(models.Model):
    c_id = models.AutoField(primary_key=True)
    gender = models.CharField(max_length=25)
    house_name = models.CharField(max_length=30)
    place = models.CharField(max_length=25)
    city = models.CharField(max_length=25)
    pin_code = models.IntegerField(db_column='pin code')  # Field renamed to remove unsuitable characters.
    email = models.CharField(max_length=25)
    phone_no = models.CharField(db_column='phone no', max_length=20)  # Field renamed to remove unsuitable characters.
    log_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'



