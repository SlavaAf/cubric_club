from django.shortcuts import render
from .models import *


# Create your tests here.


def index_view(request):
    object_list = []
    object_list = Post.objects.all()
    return render(request, 'index.html', {'object_list': object_list})