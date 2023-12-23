from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER = [
        ('guest', 'Guest'), ('admin', 'Admin')
    ]

    full_name = models.CharField(max_length = 100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 100)
    user_type = models.CharField(choices = USER, max_length =100)
    def __str__(self):
        return self.full_name