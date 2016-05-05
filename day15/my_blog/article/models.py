from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True)
    phone = models.IntegerField(null=True)
    password = models.CharField(max_length=100)


host_stat = (
    (1,"在线"),
    (0,"下线"),
)

@python_2_unicode_compatible
class HostProfile(models.Model):
    be_checked = models.BooleanField()
    hostname = models.CharField(max_length=100)
    port = models.IntegerField()
    stat = models.IntegerField(choices=host_stat)




