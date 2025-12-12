# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sa(models.Model):

    #__Sa_FIELDS__
    a = models.CharField(max_length=255, null=True, blank=True)

    #__Sa_FIELDS__END

    class Meta:
        verbose_name        = _("Sa")
        verbose_name_plural = _("Sa")



#__MODELS__END
