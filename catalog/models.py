from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')

    def __str__(self):
        return f'Name: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name')
    price = models.IntegerField(default=0, verbose_name='Price')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    bought = models.BooleanField(verbose_name='Bought')
    date = models.DateField(auto_now=True, verbose_name='Date')

    def __str__(self):
        return f'Name: {self.name} - Price: {self.price} - Category: {self.category} - Bought: {self.bought}' \
               f' - Date: {self.date}'


