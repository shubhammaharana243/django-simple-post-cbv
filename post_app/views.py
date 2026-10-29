from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Post


# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
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

class UpdatePostView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']
    template_name= 'post/update.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     return self.request.user == post.auther

class DeletePostView(DeleteView):
    pass
