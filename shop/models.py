from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f' Name: {self.name} - Price: {self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name} - Age: {self.age} - Item: {self.item_id}'




