from django.contrib import admin
from concert.models import Post, Contacts, Partners


# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'datetime']

admin.site.register(Post, AdminPost)
admin.site.register(Contacts)
admin.site.register(Partners)