from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import os

# Create your models here.
class UserProfile(User):
	user      = models.OneToOneField(User, related_name='user')
	nickname  = models.CharField(max_length=50)
	fans      = models.ManyToManyField('UserProfile', related_name='user_fans')
	following = models.ManyToManyField('UserProfile', related_name='user_following')
	portrait  = models.ImageField(upload_to=portrait_path)

	def __unicode__(self):
		return self.username

	def create_user_addition(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)
	post_save.connect(create_user_addition, sender=User)

	def portrait_path(instance, filename):
		return os.path.join('user', str(instance.username), 'portrait', filename)


admin.site.register(UserProfile)



class Inbox(models.Model):
	user = models.OneToOneField('UserProfile')



class Inbox_item(models.Model):
	inbox         = models.ForeignKey('Inbox')
	msg_type      = models.IntegerField() # 0:Create an article  1:modify an article  2:collect an ariticle
	brief_content = models.TextField()	  # JSON
	time          = models.DateTimeField(auto_now=True)


admin.site.register(Inbox_item)



class Category(models.Model):
	category_name = models.CharField(max_length=100, unique=True)
	parent        = models.ForeignKey('Category', related_name='parent_category', null=True, blank=True)

	def __unicode__(self):
		return self.category_name



class Keyword(models.Model):
	keyword_name = models.CharField(max_length=20)
	author       = models.ForeignKey('UserProfile')

	def __unicode__(self):
		return self.keyword_name

admin.site.register(Category)
admin.site.register(Keyword)



class Article_meta(models.Model):
	title          = models.CharField(max_length=200)
	category       = models.ManyToManyField('Category')
	author         = models.ForeignKey('UserProfile')
	keyword        = models.ManyToManyField('Keyword', related_name='article_meta_keyword', blank=True, null=True)
	# sited_article  = models.ManyToManyField('Article_meta', related_name='article_meta_sited_article', blank=True, null=True)
	siting_article = models.ManyToManyField('Article_meta', related_name='article_meta_siting_article', blank=True, null=True)



class Article(models.Model):
	meta       = models.ForeignKey('Article_meta')
	version    = models.PositiveIntegerField(default=0)
	content    = models.TextField(blank=True)
	time       = models.DateTimeField(auto_now=True)
	is_draft   = models.BooleanField(default=False)

	def __unicode__(self):
		return self.meta.title


admin.site.register(Article_meta)
admin.site.register(Article)



class Collection(models.Model):
	article_meta    = models.ForeignKey('Article_meta')
	article_version = models.PositiveIntegerField(default=0)
	collect_time    = models.DateTimeField(auto_now=True)
	belong_to       = models.ForeignKey('UserProfile')
	keyword         = models.ManyToManyField('Keyword')
	is_private		= models.BooleanField(default=False)

	def __unicode__(self):
		return self.article_meta.title

	class Meta:
		ordering = ['belong_to', '-collect_time']



class Comment(models.Model):
	time    = models.DateTimeField(auto_now=True)
	content = models.TextField(blank=True)
	author  = models.ForeignKey('UserProfile')
	article = models.ForeignKey('Article')


admin.site.register(Collection)
admin.site.register(Comment)



class Attachment(models.Model):
	def attachment_path(instance, filename):
		return os.path.join('attachment', str(article_meta.author), str(article_meta.title))

	attachment_type = models.CharField(max_length=100)
	attachment_file = models.FileField(upload_to=attachment_path)
	pathname        = models.CharField(max_length=255)
	article         = models.ForeignKey('Article')



class Message(models.Model):
	from_user = models.ForeignKey('UserProfile', related_name='message_from_user')
	to_user   = models.ForeignKey('UserProfile', related_name='message_to_user')
	content   = models.TextField()
	time      = models.DateTimeField(auto_now=True)
	has_read  = models.BooleanField()

	class Meta:
		ordering = ['from_user', '-time']



admin.site.register(Attachment)
admin.site.register(Message)







#Just for test
class Ticket(models.Model):
    title = models.CharField(max_length=200)
    create_ts = models.DateTimeField(auto_now_add=True)
    submitter_email = models.EmailField()
    PRIORITY_CHOICES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
    description = models.TextField()
    STATUS_CHOICES = (
        ('NEW', 'New & Unclaimed'),
        ('WIP', 'Work In Progress'),
        ('RES', 'Resolved'),
        ('CLS', 'Closed'),)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES)

    def __unicode__(self):
        return "<Ticket:%d:%s>" % (self.id, self.title,)

class TicketComment(models.Model):
    ticket = models.ForeignKey(Ticket)
    comment_ts = models.DateTimeField(auto_now_add=True)
    commenter_email = models.EmailField()
    comment = models.TextField()

    def __unicode__(self):
        return "<TicketComment:%d:%d>" % (self.ticket.id, self.id,)

admin.site.register(Ticket)
admin.site.register(TicketComment)
