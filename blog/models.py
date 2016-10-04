from __future__ import unicode_literals

from django.db import models

#class EntryQuerySet(models.QuerySet):
    #def publish(self):
        #return self.filter(publish = True)

class Entry(models.Model):
    """entry class"""
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField(max_length=200,unique = True)
    publish = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)
    #manage
    #objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
