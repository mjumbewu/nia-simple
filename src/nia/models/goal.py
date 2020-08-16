from django.db import models


class Goal (models.Model):
    label = models.TextField()
    description = models.TextField()
    values = models.ManyToManyField('Value', related_name='goals', blank=True)

    def __str__(self):
        return self.label
