from django.db import models
import os

# Create your models here.
class User(models.Model):
	# uuid       = models.CharField(max_length=200)
	username  = models.CharField(max_length=200)
	password  = models.CharField(max_length=32)		#MD5
	nickname  = models.CharField(max_length=50)
	email     = models.EmailField(max_length=200)
	fans      = models.ManyToMany('User')
	following = models.ManyToMany('User')
	portrait  = models.ImageField(upload_to=portrait_path)

	def __unicode__(self):
        return self.username

    def portrait_path(instance, filename):
    	return os.path.join('user', str(instance.username), 'portrait', filename)



class SuperAdmin(User):
	pass



class Inbox(models.Model):
	user = models.OneToOne('User')



class Inbox_item(models.Model):
	inbox         = models.ForeignKey('Inbox')
	msg_type      = models.IntegerField() # 0:Message  1:Create an article  2:modify an article
	brief_content = models.TextField()	  # JSON
	time          = models.DateTimeField(auto_now=True)



class Category(models.Model):
	category_name = models.CharField(max_length=100)

	def __unicode__(self):
        return self.category_name



class Keyword(models.Model):
	keyword_name = models.CharField(max_length=20)
	author       = models.ForeighKey('User')

	def __unicode__(self):
        return self.keyword_name



class Article_meta(models.Model):
	title          = models.CharField(max_length=200)
	category       = models.ManyToMany('Category')
	author         = models.ForeighKey('User')
	keyword        = models.ManyToMany('Keyword')
	sited_article  = models.ManyToMany('Article_meta')
	siting_article = models.ManyToMany('Article_meta')



class Article(models.Model):
	meta           = models.ForeighKey('Article_meta')
	version        = models.PositiveIntegerField(default=0)
	content        = models.TextField(blank=True)
	time           = models.DateTimeField(auto_now=True)

	def __unicode__(self):
        return self.meta.title



class Draft(Article):
	pass



class Collection(models.Model):
	article_meta    = models.ForeighKey('Article_meta')
	article_version = models.PositiveIntegerField(default=0)
	collect_time    = models.DateTimeField(auto_now=True)
	belong_to       = models.ForeighKey('User')
	keyword         = models.ManyToMany('Keyword')

	def __unicode__(self):
        return self.article_meta.title

    class Meta:
    	ordering = ['belong_to', '-collect_time']



class Comment(models.Model):
	time         = models.DateTimeField(auto_now=True)
	content      = models.TextField(blank=True)
	author       = models.ForeighKey('User')
	article_meta = models.ForeighKey('Article_meta')



class Attachment(models.Model):
	attachment_type = models.CharField(max_length=100)
	attachment_file = models.FileField(upload_to=attachment_path)
	pathname        = models.CharField(max_length=255)
	article_meta    = models.ForeighKey('Article_meta')

	def attachment_path(instance, filename):
		return os.path.join('attachment', str(article_meta.author), str(article_meta.title))



class Message(models.Model):
	from_user = models.ForeignKey('User')
	to_user   = models.ForeignKey('User')
	content   = models.TextField()
	time      = models.DateTimeField(auto_now=True)
	has_read  = models.BooleanField()

	class Meta:
    	ordering = ['from_user', '-time']


