# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.company_name)

class Job(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=2)
    job_summary = models.CharField(max_length=200)
    experience = models.CharField(max_length=200)
    benefits = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
