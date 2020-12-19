from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField

# Create your models here.

class Post(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	body = models.TextField()
	image = ResizedImageField(size=[480, 320], quality=100, upload_to='pictures', null=True, blank=True)
	video = models.FileField(upload_to='videos', null=True, blank=True)

	def __str__(self):
		return f'{self.author}: {self.body}'

	# class Meta:
	# 	verbose_name_plural = 'Posts'