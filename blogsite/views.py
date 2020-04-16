from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from . models import Status

class BlogList(ListView):
    model=Status
    template_name='home.html'

class BlogDetailView(DetailView):
    model=Status
    template_name='post_detail.html'
    context_object_name='anything_you_want'
