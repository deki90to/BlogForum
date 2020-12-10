from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . models import Post
from . forms import PostForm
# Create your views here.


class home(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-id']


class add(CreateView):
	model = Post
	template_name = 'add.html'
	form_class = PostForm
	success_url = reverse_lazy('home')


class details(DetailView):
	model = Post
	template_name = 'details.html'


class delete(DeleteView):
	model = Post
	template_name = 'delete.html'
	success_url = reverse_lazy('home')


