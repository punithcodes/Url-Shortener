from django.db import models


class Url(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(blank=True, null=True)
