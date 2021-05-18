from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    amount=models.IntegerField()
    def __str__(self):
        return f"{self.name} {self.email} {self.amount}"
class Transact(models.Model):
    senname=models.CharField(max_length=50)
    recname=models.CharField(max_length=50)
    senamt = models.IntegerField()
    curbal=models.IntegerField()