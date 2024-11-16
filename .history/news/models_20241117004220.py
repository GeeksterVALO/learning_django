from django.db import models
from django.utils.translation import gettext_lazy as _

class Tag(models.Model):
    name = models.CharField(_('name'), max_length=50, unique=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(_('title'), max_length=255)
    content = models.TextField(_('content'))
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='news', blank=True)

    def __str__(self):
        return self.title