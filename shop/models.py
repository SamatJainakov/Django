from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    price = models.IntegerField(default=0, verbose_name='Price')

    def __str__(self):
        return f' Name: {self.name} - Price: {self.price}'


class Purchase(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')
    age = models.IntegerField(default=0, verbose_name='Age')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item')

    def __str__(self):
        return f'Name: {self.name} - Age: {self.age} - Item: {self.item_id}'




