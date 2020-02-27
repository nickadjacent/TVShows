from __future__ import unicode_literals
from django.db import models


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network should be at least 3 characters"
        if len(postData['description']) < 10:
            errors["discription"] = "Description should be at least 10 characters"
        return errors


class Network(models.Model):
    name = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Show(models.Model):
    title = models.CharField(max_length=25)
    release_date = models.DateTimeField()
    description = models.TextField()
    network = models.ForeignKey(
        Network, related_name='networks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
