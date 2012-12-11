from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.conf.urls import patterns, include, url
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields
from wallet_wiki.models import *


class UserResource(ModelResource):
	following = fields.ToManyField('self', 'following', null=True, full=False)
	inbox = fields.ToOneField('wallet_wiki.resources.InboxResource', 'inbox', null=False, full=False)
	fans = fields.ToManyField('wallet_wiki.resources.UserResource', 'userprofile_set', null=True, full=False)

	class Meta:
		resource_name		  = 'user'
		queryset			   = UserProfile.objects.all()
		key_field			   = 'nickname'
		list_allowed_methods   = ['get', 'post']	
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		excludes			   = ['password', 'date_joined', 'is_active', 'is_staff', 'last_login', 'first_name', 'last_name']
		filtering = {
			'user.username': ('exact',),
			'nickname': ('exact', 'startswith',),
		}
		authentication = BasicAuthentication()
		authorization  = DjangoAuthorization()

	def prepend_urls(self):
	 	return [
	 		url(r"^(?P<resource_name>%s)/(?P<nickname>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
	 	]



class InboxResource(ModelResource):
	user = fields.ToOneField('wallet_wiki.resources.UserResource', 'user', null=False, full=False)
    feed_event = fields.ToManyField('wallet_wiki.resources.FeedEventResource', 'feedevent_set', null=True, full=True)

	class Meta:
		resource_name = 'inbox'
		queryset = Inbox.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
	
	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<user>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
		]



class CategoryResource(ModelResource):
	parent_category = fields.ForeignKey('self', 'parent', null=True, full=True)

	class Meta:
		resource_name		  = 'category'
		queryset			   = Category.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'category_name': ('exact', 'startswith', ),
		}

	authentication = Authentication()
	authorization  = Authorization()

	def override_urls(self):
		return [
			#url(r"^(?P<resource_name>%s)/(?P<category_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
			url(r"^(?P<resource_name>%s)/(?P<category_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
		]



class KeywordResource(ModelResource):
	keyword_author = fields.ToOneField('wallet_wiki.resources.UserResource', 'author', null=False, full=True)

	class Meta:
		resource_name		  = 'keyword'
		queryset			   = Keyword.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		# filtering = {
		# 	'keyword_name': ('exact', 'startswith', ),
		# }

	authentication = Authentication()
	authorization  = Authorization()
	
	def override_urls(self):
		return [
			#url(r"^(?P<resource_name>%s)/(?P<category_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
			url(r"^(?P<resource_name>%s)/(?P<author>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
		]


class ArticleMetaResource(ModelResource):
	category = fields.ToManyField('wallet_wiki.resources.CategoryResource', 'category', null=True, full=False)
	keyword	= fields.ToManyField('wallet_wiki.resources.KeywordResource', 'keyword', null=True, full=False)
	siting_article = fields.ToManyField('wallet_wiki.resources.ArticleMetaResource', 'siting_article', null=False, full=False)
	sited_article = fields.ToManyField('wallet_wiki.resources.ArticleMetaResource', 'articlemeta_set', null=False, full=False)
	author = fields.ForeignKey('wallet_wiki.resources.UserResource', 'author', null=False, full=False)
	versions = fields.ToManyField('wallet_wiki.resources.ArticleResource', 'article_set', null=False, full=False)

	class Meta:
		resource_name		  = 'article_meta'
		queryset			   = ArticleMeta.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'title': ('exact',),
			'author': ('exact', 'startswith',),
			'category': ('exact',),
		}

	authentication = Authentication()
	authorization  = Authorization()
		
	# def dehydrate(self, bundle):
	# 	this = ArticleMeta.objects.get(id=bundle.data['id'])
	# 	# get articles belonging to this article meta
	# 	versions = this.article_set.all()
	# 	if versions is not None:
	# 		bundle.data['versions'] = []
	# 		for c in versions:
	# 			bundle.data['versions'].append(c.get_absolute_url())
	# 	else:
	# 		bundle.data['versions'] = 'None'
	# 	# get sited articles
	# 	sited_articles = this.articlemeta_set.all()
	# 	if sited_articles is not None:
	# 		bundle.data['sited_articles'] = []
	# 		for c in sited_articles:
	# 			bundle.data['sited_articles'].append(c.get_absolute_url())
	# 	else:
	# 		bundle.data['sited_articles'] = 'None'
	# 	return bundle	

	def override_urls(self):
		return [
			#url(r"^(?P<resource_name>%s)/(?P<category_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
			url(r"^(?P<resource_name>%s)/user/(?P<author>[\w\d_.-]+)/(?P<title>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
		]



class ArticleResource(ModelResource):
	meta = fields.ForeignKey('wallet_wiki.resources.ArticleMetaResource', 'meta', null=False, full=False)
	comments = fields.ToManyField('wallet_wiki.resources.CommentResource', 'comment_set', null=False, full=True)
	attachments = fields.ToManyField('wallet_wiki.resources.AttachmentResource', 'attachment_set', null=False, full=True)

	class Meta:
		resource_name		  = 'article'
		queryset			   = Article.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	# def dehydrate(self, bundle):
	# 	this = Article.objects.get(id=bundle.data['id'])
	# 	# add ForeignKey comment
	# 	comments = this.comment_set.all()
	# 	if comments is not None:
	# 		bundle.data['comments'] = []
	# 		for c in comments:
	# 			bundle.data['comments'].append(c.get_absolute_url())
	# 	else:
	# 		bundle.data['comments'] = 'None'
	# 	# add ForeignKey Attachment 
	# 	attachments = this.attachment_set.all()
	# 	if attachments is not None:
	# 		bundle.data['attachments'] = []
	# 		for c in attachments:
	# 			bundle.data['attachments'].append(c.get_absolute_url())
	# 	else:
	# 		bundle.data['attachments'] = 'None'
	# 	return bundle

	authentication = Authentication()
	authorization  = Authorization()
		


class CollectionResource(ModelResource):
	article  = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)
	belong_to = fields.ForeignKey('wallet_wiki.resources.UserResource', 'belong_to', null=False, full=False)
	keyword   = fields.ToManyField('wallet_wiki.resources.KeywordResource', 'keyword', null=False, full=True)

	class Meta:
		resource_name		  = 'collection'
		queryset			   = Collection.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()
		


class CommentResource(ModelResource):
	author  = fields.ForeignKey('wallet_wiki.resources.UserResource', 'author', null=False, full=False)	
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name		  = 'comment'
		queryset			   = Comment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()



class AttachmentResource(ModelResource):
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name		  = 'attachment'
		queryset			   = Attachment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()



class MessageResource(ModelResource):
	from_user = fields.ToOneField('wallet_wiki.resources.UserResource', 'from_user', null=False, full=False)
	to_user = fields.ToOneField('wallet_wiki.resources.UserResource', 'to_user', null=False, full=False)

	class Meta:
		resource_name = 'message'
		queryset = Message.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'from_user': ('exact',),
			'to_user': ('exact',),
		}

	# TODO: this is an ugly way to add from_user and to_user to MessageResource
	#def dehydrate(self, bundle):
	#	from_user = Message.objects.get(id=bundle.data['id']).from_user
	#	to_user = Message.objects.get(id=bundle.data['id']).to_user
	#	bundle.data['from_user'] = from_user.get_absolute_url()
	#	bundle.data['to_user'] = to_user.get_absolute_url()
	#	return bundle

	authentication = Authentication()
	authorization  = Authorization()



class FeedEventResource(ModelResource):
	article = fields.ToOneField('wallet_wiki.resources.ArticleResource', 'article', null=True, full=False)
	collection = fields.ToOneField('wallet_wiki.resources.CollectionResource', 'collection', null=True, full=False)
	
	class Meta:
		resource_name = 'feedevent'
		queryset = FeedEvent.objects.all()
		list_allowed_methods = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization = Authorization()



# class ArticleEventResource(ModelResource):
# 	article = fields.ToOneField('wallet_wiki.resources.ArticleResource', 'article', null=False, full=True)
# 	
# 	class Meta:
# 		resource_name = 'articleevent'
# 		queryset = ArticleEvent.objects.all()
# 		list_allowed_methods = ['get', 'post']
# 		detail_allowed_methods = ['get', 'post', 'put', 'delete']
# 
# 	authentication = Authentication()
# 	authorization = Authorization()
# 
# 
# class CollectionEventResource(ModelResource):
# 	collection = fields.ToOneField('wallet_wiki.resources.CollectionResource', 'collection', null=False, full=True)
# 	
# 	class Meta:
# 		resource_name = 'collectionevent'
# 		queryset = CollectionEvent.objects.all()
# 		list_allowed_methods = ['get', 'post']
# 		detail_allowed_methods = ['get', 'post', 'put', 'delete']
# 		
# 
# 	authentication = Authentication()
# 	authorization = Authorization()



#Just for test
# class TicketResource(ModelResource):
#	 class Meta:
#		 queryset = Ticket.objects.all()
#		 resource_name = 'sample_ticket'
#	 def dehydrate(self, bundle):
#		 comments = TicketComment.objects.filter(ticket=bundle.data['id'])
#		 bundle.data['comments'] = [model_to_dict(c) for c in comments]
#		 return bundle

# class TicketCommentResource(ModelResource):
#	 ticket = fields.ForeignKey(TicketResource, 'ticket', full=True)
#	 class Meta:
#		 queryset = TicketComment.objects.all()
#		 resource_name = 'sample_comment'
