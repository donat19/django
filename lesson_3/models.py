from django.db import models


class Preferences(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=10000)


class Person(models.Model):
    user_name = models.CharField(max_length=10)
    user_last_name = models.CharField(max_length=10)
    age = models.IntegerField()
    status = models.BooleanField()
    file = models.FileField()
    x = models.ForeignKey(Preferences, on_delete=models.CASCADE)
