from django.db import models
from django.utils import timezone


class Post(models.Model): 
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=200)
	text = models.TextField()
	pub_date = models.DateTimeField(auto_now_add = timezone.now)
	upd_date = models.DateTimeField(auto_now_add = timezone.now)
	is_public = models.BooleanField(default=True)
	def __str__(self):
		return self.title;

class Comment(models.Model):
	author = models.CharField(max_length=50)
	text = models.CharField(max_length=50)
	pub_date = models.DateTimeField(auto_now_add = timezone.now)
	post = models.ForeignKey(Post)
	def __str__(self):
		return self.text;
