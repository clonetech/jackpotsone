from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Punter(models.Model):
    published_date = models.DateTimeField('Date Published')
    country = models.CharField(max_length = 200)
    home_team = models.CharField(max_length = 200)
    home_score = models.IntegerField(default = 0)
    away_score = models.IntegerField(default = 0)
    away_team = models.CharField(max_length = 200)
    prediction = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team

class Hexabet(models.Model):
    published_date = models.DateTimeField('Date Published')
    country = models.CharField(max_length = 200)
    home_team = models.CharField(max_length = 200)
    home_score = models.IntegerField(default = 0)
    away_score = models.IntegerField(default = 0)
    away_team = models.CharField(max_length = 200)
    safety = models.CharField(max_length = 200, default="")
    prediction = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100, choices=[('Running','Running'),('Won','Won'),('Lost','Lost')])

    def __str__(self):
       return self.home_team


class Jackpot(models.Model):
    published_date = models.DateTimeField('Date Published')
    content = models.TextField(null=True, blank=True)
    country = models.CharField(max_length = 200)
    home_team = models.CharField(max_length = 200)
    away_team = models.CharField(max_length = 200)
    home_odds = models.DecimalField(max_digits=30, decimal_places=2)
    draw_odds = models.DecimalField(max_digits=30, decimal_places=2)
    away_odds = models.DecimalField(max_digits=30, decimal_places=2)
    prediction = models.CharField(max_length = 100)


    def __str__(self):
       return self.home_team
