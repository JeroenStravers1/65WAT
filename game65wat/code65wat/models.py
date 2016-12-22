from django.db import models
import django.utils.timezone
import datetime

class RegisteredUser(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=10)
    upgrade_lvl = models.IntegerField(default=0)
    resource_x = models.IntegerField(default=100)
    resource_y = models.IntegerField(default=100)
    resource_z = models.IntegerField(default=100)
    attack_countdown = models.DateTimeField(default=django.utils.timezone.now())
    upgrade_countdown = models.DateTimeField(default=django.utils.timezone.now())
    messages = models.TextField(default="")
    last_login = models.DateTimeField(default=django.utils.timezone.now())


