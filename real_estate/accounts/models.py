# from django.db import models
# from django.contrib.auth.models import User
#
# RELEVANCE_CHOICES = (
#     (1, "buyer"),
#     (2, "seller")
# )
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     buyer_seller = models.IntegerField(choices=RELEVANCE_CHOICES)
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):
    is_seller = models.BooleanField('seller status', default=False)
    description = models.TextField(blank=True)
    register_date = models.DateTimeField(default=datetime.now, blank=True, null=True)
    photo = models.ImageField(upload_to='user', default='/home/shubham/Downloads/abc.png', null=True, blank=True)


