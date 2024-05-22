from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

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


class SignUpView(generic.CreateView):   
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html' 
