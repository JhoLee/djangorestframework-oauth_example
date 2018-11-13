from django.contrib.auth.models import User
from django.db import models


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    nickname = models.CharField(max_length=32, null=False)
