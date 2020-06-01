from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Post
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Post
    # context_object_name = 'posts'
    template_name = 'home/home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'home/detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'home/create.html'
    fields = ['title', 'user', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'home/update.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'home/delete.html'
    success_url = reverse_lazy('home')




