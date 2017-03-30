from __future__ import unicode_literals
from django.contrib.auth import models.User as ModelsUser
from django.db import models


class Users(ModelsUser):
    username = models.CharField(max_lenght=50)
    email = models.EmailField()
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField()

