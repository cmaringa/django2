# myapp/models.py
from django.db import models

class DataStatic(models.Model):
    isin = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class DataTS(models.Model):
    weight = models.FloatField()
    price = models.FloatField()
    date = models.DateField()
    data_static = models.ForeignKey(DataStatic, on_delete=models.SET_NULL,
                                null=True)
    index_symbol = models.CharField(max_length=200)

    def __str__(self):
        return self.data_static.name

    class Meta:
        ordering = ['-date']
