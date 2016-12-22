from django.db import models


class RegisteredUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)
    upgrade_lvl = models.IntegerField
    resource_x = models.IntegerField
    resource_y = models.IntegerField
    resource_z = models.IntegerField
    attack_countdown = models.DateTimeField
    upgrade_countdown = models.DateTimeField
    messages = models.TextField #TODO migrate db
    #TODO messages format: x.y.z.,
    #TODO the message content can be randomly generated on display



