from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def validateUser(self, post):

		check = True
		errors = []

		if len(post.get('name')) and len(post.get('alias')) < 3:
			check = False
			errors.append('name fields must be more than 3 characters')	
		if not re.search(r'\w+\@\w+.\w+', post.get('email')):
			check = False
			errors.append('must enter a valid email')				
		if len(post.get('password')) < 5:
			check = False
			errors.append('password must be at least 5 characters')
		if post.get('password_confirmation') != post.get('password'):
			check = False
			errors.append('password and password confirmation must match')
		return (check, errors)


class User(models.Model):
	name = models.CharField(max_length = 45)
	alias = models.CharField(max_length = 45)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	favorites = models.ManyToManyField("Quote", related_name="favorites", default=None)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return "name:{}, alias:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.name, self.alias, self.email, self.password, self.created_at, self.updated_at)

class QuoteManager(models.Manager):
	def validateQuote(self, post):

		check = True
		errors = []

		if len(post.get('content')) < 12:
			check = False
			errors.append('Message must be more than 10 characters')
		return (check, errors)

class Quote(models.Model):
	content = models.CharField(max_length = 255)
	author = models.CharField(max_length = 255)
	poster = models.ForeignKey(User, related_name = 'author')
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = QuoteManager()

	def __str__(self):
		return 'content:{}, author:{}'.format(self.content, self.user)






