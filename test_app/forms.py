from django import forms
from . models import Post, Comment


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'body', 'image', 'video')

		widgets = {
			'author':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type comment', 'rows':1, 'cols':10}),
		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			# 'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'admin', 'type':'hidden'}),

			'name': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'body'}),
			'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Post Commenting...', 'rows': 1, 'cols': 10})
		}