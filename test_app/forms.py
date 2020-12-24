from django import forms
from . models import Post


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'body', 'image', 'video', 'date')

		widgets = {
			'author':forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Type comment', 'rows':1, 'cols':10}),
		}