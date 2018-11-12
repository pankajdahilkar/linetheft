from django.db import models
class linedata(models.Model):
    cust_id=models.IntegerField()
    cust_name=models.CharField(max_length=30)
    voltage_R = models.IntegerField()
    voltage_Y = models.IntegerField()
    voltage_B = models.IntegerField()
    Ir = models.IntegerField()
    Iy = models.IntegerField()
    Ib = models.IntegerField()
    power=models.IntegerField()
    energy_consumption=models.IntegerField()
    time=models.DateTimeField(auto_now_add=True)
    date=models.DateField(auto_now=True)
