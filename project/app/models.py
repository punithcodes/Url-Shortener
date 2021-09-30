from django.db import models
from random import choices
from string import ascii_letters
from django.conf import settings

# This class is responsible for the creation of Url table in the database 
class Url(models.Model):
    original_url = models.URLField()
    short_url = models.URLField(blank=True, null=True)
    
    # This function is responsible for creating short url which is not repeated in database.
    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=5))
            new_link = settings.HOST_URL + '/' + random_string

            if not Url.objects.filter(short_url=new_link).exists():
                break
        return new_link
    
    # Here I have overridden the save method and assigning the created new url to the class variable "short_url" and saving it in database.
    def save(self, *args, **kwargs):
        if not self.short_url:
            new_link = self.shortener()
            self.short_url = new_link
        return super().save(*args, **kwargs)
