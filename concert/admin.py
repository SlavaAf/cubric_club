from django.contrib import admin
from concert.models import Post

# Register your models here.
class AdminPost(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Post, AdminPost)