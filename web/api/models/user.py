from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 第三方登录提供商
    provider = models.CharField(max_length=255, null=True, blank=True)
    # 第三方登录用户ID
    uid = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username
