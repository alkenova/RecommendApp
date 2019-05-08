from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from api.helpers import constants


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    password = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    birth_date = models.DateTimeField()
    # status = models.CharField(choices=constants.USER_STATUS, default='GUEST')
    gender = models.CharField(choices=constants.GENDER_CHOICES, max_length=6)
    address = models.TextField()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.email