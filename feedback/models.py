from django.db import models

# Create your models here.
class Feedback(models.Model):
    f_id = models.AutoField(primary_key=True)
    o_id = models.IntegerField()
    feedback = models.CharField(max_length=30)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'feedback'
