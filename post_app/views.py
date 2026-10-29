from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

class PostDetailView(DeleteView):
    model = Post
    template_name = 'post/detail.html'

class CreatePostView(CreateView, LoginRequiredMixin):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)


class DeletePostView(DeleteView):
    pass
