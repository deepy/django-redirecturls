from django.db import models

class Shorturls(models.Model):
    shortname = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=400, help_text="The URI to redirect to.")

    class Meta:
        ordering = ('shortname',)
        verbose_name = "Short URI"
    def __unicode__(self): 
        return self.shortname

