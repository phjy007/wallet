from django.db import models
from django.contrib import admin
from django.db.models.signals import post_save
from django.contrib.auth.models import User
import os


ARTICLE_ACTION_CHOICES = (
	('create', u'create'),
	('update', u'update'),
	('share',  u'share'),
)

# Create your models here.
class UserProfile(models.Model):
	def portrait_path(instance, filename):
		return os.path.join('user', str(instance.user.username), 'portrait', filename)

	user      = models.OneToOneField(User)
	nickname  = models.CharField(max_length=50)
	following = models.ManyToManyField('self', blank=True, null=True, symmetrical=False)
	portrait  = models.ImageField(upload_to=portrait_path, blank=True, null=True)

	def __unicode__(self):
		return self.nickname 

	def create_user_profile(sender, instance, created, **kwargs):
		if created:  
			profile, created = UserProfile.objects.get_or_create(user=instance)
	post_save.connect(create_user_profile, sender=User)

	def get_absolute_url(self):
		from wallet.urls import v1_api
		return '/api/' + v1_api.api_name + '/user/' + str(self.id) + '/'

def user_post_save_callbalck(sender, instance, created, **kwargs):
	if issubclass(sender, UserProfile):
		if created:
			inbox, created = Inbox.objects.get_or_create(user=instance)

post_save.connect(user_post_save_callbalck, dispatch_uid="my_unique_identifier_1")


admin.site.register(UserProfile)



# Inbox is the contatin for FeedMessages
INBOX_MAX_ITEM = 2
class Inbox(models.Model):
	user = models.OneToOneField('UserProfile')

	def __unicode__(self):
		return str(self.user.user.username) + ' Inbox'


admin.site.register(Inbox)



class Category(models.Model):
	category_name = models.CharField(max_length=100, unique=True)
	parent        = models.ForeignKey('self', null=True, blank=True)

	def __unicode__(self):
		return self.category_name



class Keyword(models.Model):
	keyword_name = models.CharField(max_length=20)
	author       = models.ForeignKey('UserProfile', null=False, blank=False)

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
		return str(self.title)

	def get_absolute_url(self):
		from wallet.urls import v1_api
		return '/api/' + v1_api.api_name + '/article_meta/' + str(self.id) + '/'



class Article(models.Model):
	meta       = models.ForeignKey('ArticleMeta')
	version    = models.PositiveIntegerField(default=0)
	content    = models.TextField(blank=True)
	time       = models.DateTimeField(auto_now=True)
	is_draft   = models.BooleanField(default=False)

	def __unicode__(self):
		return str(self.meta.title) + ' v' + str(self.version)

	def get_absolute_url(self):
		from wallet.urls import v1_api
		return '/api/' + v1_api.api_name + '/article/' + str(self.id) + '/'

def article_post_save_callbalck(sender, instance, created, **kwargs):
	if issubclass(sender, Article):
		if created:
			author = instance.meta.author
			fans   = author.userprofile_set.all()
			for c in fans:
				inbox = c.inbox
				feedevent_list = inbox.feedevent_set.all() # The FeedEvents in the feedevent_list are ordered by time reversely.
				feed_item_count = len(feedevent_list)
				if feed_item_count >= INBOX_MAX_ITEM:
					# print c
					# for a in feedevent_list:
					# 	print a.time
					oldest_event = feedevent_list[INBOX_MAX_ITEM-1]
					oldest_event.delete()
				if instance.version == 0:
					action = ARTICLE_ACTION_CHOICES[0][1] # create a new article
				else:
					action = ARTICLE_ACTION_CHOICES[1][1] # update a new version of certain article
				article_event = ArticleEvent.objects.create(inbox=inbox, action=action, article=instance)
				article_event.save

post_save.connect(article_post_save_callbalck, dispatch_uid="my_unique_identifier_2")



admin.site.register(ArticleMeta)
admin.site.register(Article)



class Collection(models.Model):
	article           = models.ForeignKey('Article')
	collect_time      = models.DateTimeField(auto_now=True)
	belong_to         = models.ForeignKey('UserProfile')
	keyword           = models.ManyToManyField('Keyword', null=True, blank=True)
	is_private        = models.BooleanField(default=False)

	def __unicode__(self):
		return self.belong_to.user.username + ' -> ' + self.article.meta.title + ' v' + str(self.article.version)

	class Meta:
		ordering = ['belong_to', '-collect_time']

def collect_post_save_callbalck(sender, instance, created, **kwargs):
	if issubclass(sender, Collection):
		if created:
			if not instance.is_private:
				collector = instance.belong_to
				fans      = collector.userprofile_set.all()
				for c in fans:
					print c
					inbox = c.inbox
					feedevent_list = inbox.feedevent_set.all()
					feed_item_count = len(feedevent_list)
					if feed_item_count >= INBOX_MAX_ITEM:
						# print c
						# for a in feedevent_list:
						# 	print a.time
						oldest_event = feedevent_list[INBOX_MAX_ITEM-1]
						oldest_event.delete()
					collection_event = CollectionEvent.objects.create(inbox=inbox, collection=instance)
					collection_event.save

post_save.connect(collect_post_save_callbalck)#, dispatch_uid="my_unique_identifier_3"



class Comment(models.Model):
	time    = models.DateTimeField(auto_now=True)
	content = models.TextField(blank=True)
	author  = models.ForeignKey('UserProfile')
	article = models.ForeignKey('Article')

	def __unicode__(self):
		return self.article.meta.title + ' v' + str(self.article.version)

	def get_absolute_url(self):
		from wallet.urls import v1_api
		return '/api/' + v1_api.api_name + '/comment/' + str(self.id) + '/'


admin.site.register(Collection)
admin.site.register(Comment)



class Attachment(models.Model):
	def attachment_path(instance, filename):
		return os.path.join('attachment', str(instance.article.meta.author.user.username), str(instance.article.meta.title), filename)

	attachment_type = models.CharField(max_length=100)
	attachment_file = models.FileField(upload_to=attachment_path)
	article         = models.ForeignKey('Article')

	def __unicode__(self):
		return self.article.meta.title + ' v' + str(self.article.version)

	def get_absolute_url(self):
		from wallet.urls import v1_api
		return '/api/' + v1_api.api_name + '/attachment/' + str(self.id) + '/'



# User-to-User messages
class Message(models.Model):
	from_user = models.OneToOneField('UserProfile', related_name='from_user')
	to_user   = models.OneToOneField('UserProfile', related_name='to_user')
	content   = models.TextField()
	has_read  = models.BooleanField(default=False)
	time      = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.from_user.user.username + ' -> ' + self.to_user.user.username

	class Meta:
		ordering = ['from_user', '-time']

	

# Feed in one User's inbox
class FeedEvent(models.Model):
	inbox = models.ForeignKey('Inbox')
	time  = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-time']

class ArticleEvent(FeedEvent):
	action  = models.CharField(max_length=20, default='create', choices=ARTICLE_ACTION_CHOICES)
	article = models.ForeignKey('Article')	

	def __unicode__(self):
		return self.inbox.user.user.username + '\'s ARTICLE FEED: ' + self.article.meta.title + ' ----> ACTION: ' + self.action


# Public collection action will be posted to the inboxes of collector's fans
class CollectionEvent(FeedEvent):
	collection = models.ForeignKey('Collection')

	def __unicode__(self):
		return self.inbox.user.user.username + '\'s COLLECTION FEED: ' + ' collects ' + str(self.collection)


# can be extended
class CommentEvent(FeedEvent):
	pass


# can be extended
class FollowEvent(FeedEvent):
	pass



admin.site.register(Attachment)
admin.site.register(Message)
admin.site.register(ArticleEvent)
admin.site.register(CollectionEvent)







#Just for test
# class Ticket(models.Model):
#     title = models.CharField(max_length=200)
#     create_ts = models.DateTimeField(auto_now_add=True)
#     submitter_email = models.EmailField()
#     PRIORITY_CHOICES = (
#         ('H', 'High'),
#         ('M', 'Medium'),
#         ('L', 'Low'),)
#     priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
#     description = models.TextField()
#     STATUS_CHOICES = (
#         ('NEW', 'New & Unclaimed'),
#         ('WIP', 'Work In Progress'),
#         ('RES', 'Resolved'),
#         ('CLS', 'Closed'),)
#     status = models.CharField(max_length=3, choices=STATUS_CHOICES)

#     def __unicode__(self):
#         return "<Ticket:%d:%s>" % (self.id, self.title,)

# class TicketComment(models.Model):
#     ticket = models.ForeignKey(Ticket)
#     comment_ts = models.DateTimeField(auto_now_add=True)
#     commenter_email = models.EmailField()
#     comment = models.TextField()

#     def __unicode__(self):
#         return "<TicketComment:%d:%d>" % (self.ticket.id, self.id,)

# admin.site.register(Ticket)
# admin.site.register(TicketComment)

# class Region(models.Model):  
#     parent = models.ForeignKey('self', null=True, blank=True)  
#     name = models.CharField(max_length=30)  
#     region_type = models.IntegerField()

#     def __unicode__(self):
#     	return self.name

# admin.site.register(Region)

