from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

class Tag(models.Model):
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.slug

#????
class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish = True)

class Entry(models.Model):
    """entry class"""
    title = models.CharField(max_length = 200)
    body = models.TextField()
    slug = models.SlugField(max_length=200,unique = True)
    publish = models.BooleanField(default=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    #manage
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("entry_detail",kwargs = {"slug":self.slug})

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
