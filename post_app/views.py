from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.http import HttpResponse
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

class PostDetailView(DeleteView):
    pass

class CreatePostView(CreateView):
    pass

class DeletePostView(DeleteView):
    pass
