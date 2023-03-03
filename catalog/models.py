from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'Name: {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    bought = models.BooleanField(verbose_name='Bought')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f'Name: {self.name} - Price: {self.price} - Category: {self.category} - Bought: {self.bought}' \
               f' - Date: {self.date}'


