from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from . models import Post, Comment
from . forms import PostForm, CommentForm
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

class update(UpdateView):
	model = Post
	form_class = PostForm
	template_name = 'update.html'
	success_url = reverse_lazy('home')

class add_comment(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	success_url = reverse_lazy('home')
	ordering = ['-id']

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)