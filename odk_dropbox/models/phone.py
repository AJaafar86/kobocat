#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4 encoding=utf-8

from django.db import models

class Phone(models.Model):
    imei = models.CharField(max_length=32, unique=True)

    class Meta:
        app_label = 'odk_dropbox'

    def __unicode__(self):
        return self.device_id
