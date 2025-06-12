from django.db import models


class AvatarItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_items/')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class ComputerItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shop_items/computer_items/')
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name