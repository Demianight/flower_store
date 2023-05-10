from django.db import models
from users.models import User


"""
There is also second way to divide Offer and Flower to different models
Divided variant include kinda complex link between flower and it's amount
But provide better handling of price_for_one field
I choose easier **for development** way that includes everything in one model
Also in future divided variant would be waaaay more comfortable to use
Sorry for long comment)))

P.S. Okay I could not leave it like that, check models_extra.py
"""


class Offer(models.Model):
    """
    Model for declaring seller's offer.
    Includes flower params.
    """
    RED: str = 'red'
    YELLOW: str = 'yellow'
    BLUE: str = 'blue'
    ORANGE: str = 'orange'
    WHITE: str = 'white'

    CHOICES = (
        (RED, 'red'),
        (YELLOW, 'yellow'),
        (BLUE, 'blue'),
        (ORANGE, 'orange'),
        (WHITE, 'white'),
    )

    name = models.CharField(max_length=128)
    shade = models.CharField(max_length=128, choices=CHOICES)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    flower_amount = models.SmallIntegerField()
    price = models.SmallIntegerField()
    price_for_one = models.SmallIntegerField()
    hidden = models.BooleanField()

    def __str__(self) -> str:
        return self.name


class Trade(models.Model):
    """
    Connects Buyer Seller and Offer instances to declare trade.
    """
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='trades'
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sells'
    )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE, related_name='appears_at'
    )

    def __str__(self) -> str:
        return f'{self.offer.name} {self.offer.flower_amount}'


class OfferReview(models.Model):
    message = models.TextField()
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
    offer = models.ForeignKey(
        Offer, on_delete=models.CASCADE,
    )


class SellerReview(models.Model):
    message = models.TextField()
    reviewer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews'
    )
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE,
    )
