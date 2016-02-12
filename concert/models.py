# coding: utf-8
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    ACCOUNT_TYPES = (
        (1, u'Концерт'),
        (2, u'Вечеринка'),
    )
    title = models.CharField(verbose_name="Заголовок", max_length=100, default="") # заголовок превью
    preview_text = models.TextField(verbose_name="Текст превью", default="") # текст превью
    ticket_price = models.IntegerField(verbose_name="Цена билета", default=0) # цена билета
    ticket_vip_price = models.IntegerField(verbose_name="Цена VIP билета", default=0) # цена вип-билета
    event_type = models.IntegerField(verbose_name='Тип аккаунта', default=1, choices=ACCOUNT_TYPES) # тип события
    preview_image = models.ImageField(verbose_name="Изображение превью", blank=True) # картинка в превью
    video_link = models.CharField(verbose_name="Ссылка на видео", max_length=200, default="", blank=True) # ссылка на видео
    ticket_link = models.CharField(verbose_name="Ссылка на билет", max_length=200, default="", blank=True) # ссылка на билет

    datetime = models.DateTimeField('Дата') # дата начала концерта
    full_desc_ck = RichTextUploadingField(verbose_name="Полное описание со стилем", blank=True) # полное описание в ckeditor
    full_desc = models.TextField(verbose_name="Полное описание без стилей", default="", blank=True) # полное описание без ckeditor

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

