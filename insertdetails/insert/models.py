from django.db import models

# Create your models here.
class insert(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=100)
    deg=models.CharField(max_length=100)
    salary=models.IntegerField()
    email=models.EmailField()
    place=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    photo=models.ImageField(upload_to="image/")

class Meta:
    db_table="insert"