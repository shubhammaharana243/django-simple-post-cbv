from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.http import HttpResponse

# Create your views here.

class PostListView(ListView):
    pass

class PostDetailView(DeleteView):
    pass

class CreatePostView(CreateView):
    pass

class DeletePostView(DeleteView):
    pass
