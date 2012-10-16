from django.db import models
from django.contrib import admin
import os

# Create your models here.
class User(models.Model):
	def portrait_path(instance, filename):
		return os.path.join('user', str(instance.username), 'portrait', filename)

	# uuid       = models.CharField(max_length=200)
	username  = models.CharField(max_length=200)
	password  = models.CharField(max_length=32)		#MD5
	nickname  = models.CharField(max_length=50)
	email     = models.EmailField(max_length=200)
	fans      = models.ManyToManyField('User', related_name='user_fans')
	following = models.ManyToManyField('User', related_name='user_following')
	portrait  = models.ImageField(upload_to=portrait_path)

	def __unicode__(self):
		return self.username

	

class Super_admin(User):
	pass

admin.site.register(User)
admin.site.register(SuperAdmin)



class Inbox(models.Model):
	user = models.OneToOneField('User')



class Inbox_item(models.Model):
	inbox         = models.ForeignKey('Inbox')
	msg_type      = models.IntegerField() # 0:Message  1:Create an article  2:modify an article
	brief_content = models.TextField()	  # JSON
	time          = models.DateTimeField(auto_now=True)

admin.site.register(Inbox)
admin.site.register(Inbox_item)



class Category(models.Model):
	category_name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.category_name



class Keyword(models.Model):
	keyword_name = models.CharField(max_length=20)
	author       = models.ForeignKey('User')

	def __unicode__(self):
		return self.keyword_name

admin.site.register(Category)
admin.site.register(Keyword)



class Article_meta(models.Model):
	title          = models.CharField(max_length=200)
	category       = models.ManyToManyField('Category')
	author         = models.ForeignKey('User')
	keyword        = models.ManyToManyField('Keyword', related_name='article_meta_keyword')
	sited_article  = models.ManyToManyField('Article_meta', related_name='article_meta_sited_article')
	siting_article = models.ManyToManyField('Article_meta', related_name='article_meta_siting_article')



class Article(models.Model):
	meta           = models.ForeignKey('Article_meta')
	version        = models.PositiveIntegerField(default=0)
	content        = models.TextField(blank=True)
	time           = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.meta.title



class Draft(Article):
	pass


admin.site.register(Article_meta)
admin.site.register(Article)
admin.site.register(Draft)



class Collection(models.Model):
	article_meta    = models.ForeignKey('Article_meta')
	article_version = models.PositiveIntegerField(default=0)
	collect_time    = models.DateTimeField(auto_now=True)
	belong_to       = models.ForeignKey('User')
	keyword         = models.ManyToManyField('Keyword')

	def __unicode__(self):
		return self.article_meta.title

	class Meta:
		ordering = ['belong_to', '-collect_time']



class Comment(models.Model):
	time         = models.DateTimeField(auto_now=True)
	content      = models.TextField(blank=True)
	author       = models.ForeignKey('User')
	article_meta = models.ForeignKey('Article_meta')


admin.site.register(Collection)
admin.site.register(Comment)



class Attachment(models.Model):
	def attachment_path(instance, filename):
		return os.path.join('attachment', str(article_meta.author), str(article_meta.title))

	attachment_type = models.CharField(max_length=100)
	attachment_file = models.FileField(upload_to=attachment_path)
	pathname        = models.CharField(max_length=255)
	article_meta    = models.ForeignKey('Article_meta')



class Message(models.Model):
	from_user = models.ForeignKey('User', related_name='message_from_user')
	to_user   = models.ForeignKey('User', related_name='message_to_user')
	content   = models.TextField()
	time      = models.DateTimeField(auto_now=True)
	has_read  = models.BooleanField()

	class Meta:
		ordering = ['from_user', '-time']


admin.site.register(Attachment)
admin.site.register(Message)
