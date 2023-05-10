from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    CUSTOMER: str = 'user'
    SELLER: str = 'moderator'

    CHOICES = (
        (CUSTOMER, 'customer'),
        (SELLER, 'seller'),
    )

    role = models.CharField(choices=CHOICES, default='user', max_length=128)

    @property
    def is_customer(self) -> bool:
        return self.role == self.CUSTOMER

    @property
    def is_seller(self) -> bool:
        return self.role == self.SELLER

    def __str__(self) -> str:
        return self.username

    @classmethod
    def make_list(cls):
        users = User.objects.all()
        return [
            [
                user, [*user.sells.all()], user.sells.aggregate(
                    models.Sum('offer__price')
                )['offer__price__sum']
            ] for user in users
        ]
