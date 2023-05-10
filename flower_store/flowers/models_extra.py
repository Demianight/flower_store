from django.db import models
from users.models import User


"""
I don't know much about it but it seems like much more complex way to handle
by frontend (creating flower and offer instances seperately)
"""


class Flower(models.Model):
    FAKE_CHOICES = ()

    name = models.CharField(max_length=128)
    shade = models.CharField(choices=FAKE_CHOICES, max_length=128)
    price = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Offer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.SmallIntegerField()
    hidden = models.BooleanField()
    amount = models.SmallIntegerField()
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
