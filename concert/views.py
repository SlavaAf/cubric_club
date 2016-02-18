from django.shortcuts import render
from .models import *
import datetime


# Create your tests here.


def index_view(request):
    object_list = Post.objects.all()
    result_list = []
    for obj in object_list:
        actual = True if datetime.datetime(obj.datetime.year, obj.datetime.month,
                                           obj.datetime.day, obj.datetime.hour,
                                           obj.datetime.minute) > datetime.datetime.now() else False
        if actual:
            result_obj = {'event_type': obj.event_type, 'datetime': obj.datetime,
                          'preview_image': obj.preview_image, 'title': obj.title, 'preview_text': obj.preview_text,
                          'ticket_price': obj.ticket_price, 'ticket_vip_price': obj.ticket_vip_price,
                          'ticket_link': obj.ticket_link, 'pk': obj.pk,
                          }

            result_list.append(result_obj)
    return render(request, 'index.html', {'object_list': result_list})


def contact_view(request):
    object_list = Post.objects.all()
    result_list = []
    for obj in object_list:
        actual = True if datetime.datetime(obj.datetime.year, obj.datetime.month,
                                           obj.datetime.day, obj.datetime.hour,
                                           obj.datetime.minute) > datetime.datetime.now() else False
        if actual:
            result_obj = {'event_type': obj.event_type, 'datetime': obj.datetime,
                          'preview_image': obj.preview_image, 'title': obj.title, 'preview_text': obj.preview_text,
                          'ticket_price': obj.ticket_price, 'ticket_vip_price': obj.ticket_vip_price,
                          'ticket_link': obj.ticket_link, 'pk': obj.pk,
                          }

            result_list.append(result_obj)
    return render(request, 'contact.html', {'object_list': result_list})


def about_view(request):
    object_list = Post.objects.all()
    result_list = []
    for obj in object_list:
        actual = True if datetime.datetime(obj.datetime.year, obj.datetime.month,
                                           obj.datetime.day, obj.datetime.hour,
                                           obj.datetime.minute) > datetime.datetime.now() else False
        if actual:
            result_obj = {'event_type': obj.event_type, 'datetime': obj.datetime,
                          'preview_image': obj.preview_image, 'title': obj.title, 'preview_text': obj.preview_text,
                          'ticket_price': obj.ticket_price, 'ticket_vip_price': obj.ticket_vip_price,
                          'ticket_link': obj.ticket_link, 'pk': obj.pk,
                          }

            result_list.append(result_obj)
    return render(request, 'about.html', {'object_list': result_list})


def detail_view(request, pk):
    event = Post.objects.get(pk=pk)
    object_list = Post.objects.all()
    result_list = []
    for obj in object_list:
        actual = True if datetime.datetime(obj.datetime.year, obj.datetime.month,
                                           obj.datetime.day, obj.datetime.hour,
                                           obj.datetime.minute) > datetime.datetime.now() else False
        if actual:
            result_obj = {'event_type': obj.event_type, 'datetime': obj.datetime,
                          'preview_image': obj.preview_image, 'title': obj.title, 'preview_text': obj.preview_text,
                          'ticket_price': obj.ticket_price, 'ticket_vip_price': obj.ticket_vip_price,
                          'ticket_link': obj.ticket_link, 'pk': obj.pk,
                          }

            result_list.append(result_obj)
    return render(request, 'event_detail.html', {'event': event, 'object_list': result_list})

