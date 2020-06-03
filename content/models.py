from django.db import models
from django.contrib import admin

# Create your models here.


class Match(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)
    notes = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return 'Matching Organization: ' + self.name

    class Meta:
        ordering = ['created']
        verbose_name = 'Matching Organization'


class Contribute(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return 'Contributing Organization: ' + self.name

    class Meta:
        ordering = ['created']
        verbose_name = 'Contributing Organization'

# Register the models to the admin site


admin.site.register(Match)
admin.site.register(Contribute)
