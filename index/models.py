from django.db import models

class People (models.Model):
    name = models.CharField(max_length=100, null=True, blank=False)
    def __str__(self):
        return str(self.name)