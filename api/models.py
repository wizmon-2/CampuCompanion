from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import AccountManager

class Accounts(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'institution'),
    )
    iid = models.IntegerField()
    userid = models.IntegerField(unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    groups = models.JSONField()

    name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'userid'
    REQUIRED_FIELDS = ['iid', 'name', 'user_type']

    objects = AccountManager()

    def __str__(self):
        return self.name