from django.db import models


class Value (models.Model):
    label = models.TextField()
    description = models.TextField()
