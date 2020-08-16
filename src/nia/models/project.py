from django.db import models


class Project (models.Model):
    label = models.TextField()
    description = models.TextField()
    goals = models.ManyToManyField('Goal', related_name='projects')
