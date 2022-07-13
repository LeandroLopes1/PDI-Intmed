from django.db import models


class LoginUserModel(models.Model):
    access = models.TextField()
    refresh = models.TextField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
