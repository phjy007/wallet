from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import os

# Create your models here.
class UserProfile(User):
	def portrait_path(instance, filename):
		return os.path.join('user', str(instance.username), 'portrait', filename)

	user      = models.OneToOneField(User, related_name='user')
	nickname  = models.CharField(max_length=50)
	following = models.ManyToManyField('UserProfile', blank=True, null=True)
	portrait  = models.ImageField(upload_to=portrait_path, blank=True, null=True)

	def __unicode__(self):
		return self.username

	def create_user_addition(sender, instance, created, **kwargs):
		if created:
			UserProfile.objects.create(user=instance)
	post_save.connect(create_user_addition, sender=User)

admin.site.register(UserProfile)



# To add UserProfile's fileds to Django-User-Admin Web Interface ---------------------------------
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
class UserProfileInline(admin.StackedInline):
	model               = UserProfile
	can_delete          = False
	verbose_name_plural = 'profile'
# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
# -------------------------------------------------------------------------------------------------



class Inbox(models.Model):
	user = models.OneToOneField('UserProfile')

	def __unicode__(self):
		return str(self.user.username) + ' Inbox'



class InboxItem(models.Model):
	inbox         = models.ForeignKey('Inbox')
	msg_type      = models.IntegerField() # 0:Create an article  1:modify an article  2:collect an ariticle
	brief_content = models.TextField()	  # JSON
	time          = models.DateTimeField(auto_now=True)


admin.site.register(Inbox)
admin.site.register(InboxItem)



class Category(models.Model):
	category_name = models.CharField(max_length=100, unique=True)
	parent        = models.ForeignKey('self', null=True, blank=True)

	def __unicode__(self):
		return self.category_name



class Keyword(models.Model):
	keyword_name = models.CharField(max_length=20)
	author       = models.ForeignKey('UserProfile')

	def __unicode__(self):
		return self.keyword_name


admin.site.register(Category)
admin.site.register(Keyword)



class ArticleMeta(models.Model):
	title          = models.CharField(max_length=200)
	category       = models.ManyToManyField('Category')
	author         = models.ForeignKey('UserProfile')
	keyword        = models.ManyToManyField('Keyword', blank=True, null=True)
	siting_article = models.ManyToManyField('ArticleMeta', blank=True, null=True)

	def __unicode__(self):
		return  'META -' + str(self.title)



class Article(models.Model):
	meta       = models.ForeignKey('ArticleMeta')
	version    = models.PositiveIntegerField(default=0)
	content    = models.TextField(blank=True)
	time       = models.DateTimeField(auto_now=True)
	is_draft   = models.BooleanField(default=False)

	def __unicode__(self):
		return 'ARTICLE -' + str(self.meta.title)


admin.site.register(ArticleMeta)
admin.site.register(Article)



class Collection(models.Model):
	article_meta    = models.ForeignKey('ArticleMeta')
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
	from_user = models.OneToOneField('UserProfile', related_name='from_user')
	to_user   = models.OneToOneField('UserProfile', related_name='to_user')
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

class Region(models.Model):  
    parent = models.ForeignKey('self', null=True, blank=True)  
    name = models.CharField(max_length=30)  
    region_type = models.IntegerField()

    def __unicode__(self):
    	return self.name

admin.site.register(Region)

