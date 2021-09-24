from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings


class Url(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(blank=True, null=True)

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=5))
            new_link = settings.HOST_URL + '/' + random_string

            if not Url.objects.filter(short_url=new_link).exists():
                break
        return new_link

    def save(self, *args, **kwargs):
        if not self.short_url:
            new_link = self.shortener()
            self.short_url = new_link
        return super().save(*args, **kwargs)
