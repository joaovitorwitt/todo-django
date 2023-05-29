from django.db import models

# Create your models here.

class recordUsers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    nickname = models.CharField(max_length=50)
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.nickname