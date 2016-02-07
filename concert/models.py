# coding: utf-8
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title = models.CharField(max_length=100)
    datetime = models.DateTimeField('Дата публикации')
    desc = RichTextUploadingField()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

admin.site.register(Post)