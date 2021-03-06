# coding: utf-8
import re
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Contacts(models.Model):
    description = RichTextUploadingField(verbose_name="Контакты", blank=True)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Partners(models.Model):
    description = RichTextUploadingField(verbose_name="Партнеры", blank=True)

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"


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

    datetime = models.DateTimeField('Дата', ) # дата начала концерта
    full_desc_ck = RichTextUploadingField(verbose_name="Полное описание со стилем", blank=True) # полное описание в ckeditor
    full_desc = models.TextField(verbose_name="Полное описание без стилей", default="", blank=True) # полное описание без ckeditor

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    def save(self, *args, **kwargs):
        t = self.video_link
        if self.video_link.find("embed") < 0:
            re_str = r"((?<=(v|V)\/)|(?<=be\/)|(?<=(\?|\&)v=)|(?<=embed))([\w-]+)"
            k = re.findall(re_str, self.video_link)
            if len(k) > 0:
                for key in k[0]:
                    if len(key) == 11:
                        t = "http://youtube.com/embed/" + key
        self.video_link = t
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"

