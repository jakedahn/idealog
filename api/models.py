from django.db import models
from django.contrib.auth.models import User


class Idea(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=30, null=True, blank=False)
    description = models.TextField(blank=False)  # elevator pitch


class Note(models.Model):
    user = models.ForeignKey(User)
    idea = models.ForeignKey(Idea, related_name='notes')
    body = models.TextField(blank=False)
