#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

class Xss(models.Model):
    cookie = models.CharField(max_length=10000)

    def __unicode__(self):
        return self.cookie
