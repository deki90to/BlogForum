from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from datetime import datetime
# Create your models here.


class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	image = ResizedImageField(size=[480, 320], quality=100, upload_to='pictures', null=True, blank=True)
	video = models.FileField(upload_to='videos', null=True, blank=True)
	date = models.DateTimeField(default=datetime.now)

	def __str__(self):
		return f'{self.author}: {self.body}'

	# class Meta:
	# 	verbose_name_plural = 'Posts'

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	body = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-date']

	def __str__(self):
		return '%s - %s' % (self.name, self.post.body)