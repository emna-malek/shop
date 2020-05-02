from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    postal_code = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    width_field = models.IntegerField(null=True, blank=True, default=0)
    height_field = models.IntegerField(null=True, blank=True, default=0)
    city = models.CharField(max_length=100, default='')
    company = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = userProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
