from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView,ListView
# Create your views here.


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list'



# class HomePageView(TemplateView):
#     template_name = 'home.html'




class AboutPageView(TemplateView):
    template_name = 'about.html'