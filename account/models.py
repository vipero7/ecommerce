from django.db import models
from django.conf import settings
from django.urls import reverse
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%y/%m/%d', blank=True)
    phone_no = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('account:user_profile', args=[self.username])