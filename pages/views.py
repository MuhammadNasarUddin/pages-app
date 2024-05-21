from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView

class PostListView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'body', 'author']
    success_url = '/'

class PostCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'body', 'author']
    success_url = '/'
