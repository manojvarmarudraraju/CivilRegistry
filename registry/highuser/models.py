from django.db import models

# Create your models here.
class verify(models.Model):
    adminid=models.CharField(max_length=13);
    userid=models.CharField(max_length=13);
    veridate=models.DateField();
    def __str__(self):
        return self.userid