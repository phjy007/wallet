from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.conf.urls import patterns, include, url
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields
from tastypie.resources import ALL_WITH_RELATIONS
from wallet_wiki.models import *


class UserResource(ModelResource):
	user = fields.ToOneField('wallet_wiki.resources.UserCoreResource', 'user', null=False, full=True)
	following = fields.ToManyField('self', 'following', null=True, full=False)
	inbox = fields.ToOneField('wallet_wiki.resources.InboxResource', 'inbox', null=False, full=False)
	fans = fields.ToManyField('wallet_wiki.resources.UserResource', 'userprofile_set', null=True, full=False)

	class Meta:
		resource_name		  = 'user'
		queryset			   = UserProfile.objects.all()
		key_field			   = 'nickname'
		list_allowed_methods   = ['get', 'post']	
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'user': ALL_WITH_RELATIONS,
			'nickname': ('exact', 'startswith', ),
		}
		# authentication = BasicAuthentication()
		# authorization  = DjangoAuthorization()
		authentication = Authentication()
		authorization  = Authorization()


	def override_urls(self):
	 	return [
	 		url(r"^(?P<resource_name>%s)/(?P<user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
	 	]
		

class UserCoreResource(ModelResource):

	class Meta:
		resource_name = 'user_core'
		queryset = User.objects.all()
		excludes = ['password', 'date_joined', 'is_active', 'is_staff', 'last_login', 'first_name', 'last_name']
		filtering = {
			'username': ('exact', ),		
		}
		
		authentication = Authentication()
		authorization  = Authorization()

	def override_urls(self):
	 	return [
	 		url(r"^(?P<resource_name>%s)/(?P<username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
	 	]



class InboxResource(ModelResource):
	user = fields.ToOneField('wallet_wiki.resources.UserResource', 'user', null=False, full=False)
	feed_event = fields.ToManyField('wallet_wiki.resources.FeedEventResource', 'feedevent_set', null=True, full=False)

	class Meta:
		resource_name = 'inbox'
		queryset = Inbox.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'user': ALL_WITH_RELATIONS,
		}
	
	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<user__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
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

	def prepend_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<category_name>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
		]



class KeywordResource(ModelResource):
	keyword_author = fields.ToOneField('wallet_wiki.resources.UserResource', 'author', null=False, full=False)

	class Meta:
		resource_name		  = 'keyword'
		queryset			   = Keyword.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'user': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()
	
	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<author__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
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
			'id': ('exact', ),
			'title': ('exact', 'startswith'),
			'author': ALL_WITH_RELATIONS,
			'category': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()
		
	def override_urls(self):
		return [
			# url(r"^(?P<resource_name>%s)/(?P<author__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
			url(r"^(?P<resource_name>%s)/(?P<author__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class ArticleResource(ModelResource):
	meta = fields.ForeignKey('wallet_wiki.resources.ArticleMetaResource', 'meta', null=False, full=False)
	comments = fields.ToManyField('wallet_wiki.resources.CommentResource', 'comment_set', null=False, full=False)
	attachments = fields.ToManyField('wallet_wiki.resources.AttachmentResource', 'attachment_set', null=False, full=False)

	class Meta:
		resource_name		  = 'article'
		queryset			   = Article.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'meta': ALL_WITH_RELATIONS,
			'id': ('exact', ),
		}

	authentication = Authentication()
	authorization  = Authorization()
		
	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<meta__author__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class CollectionResource(ModelResource):
	article  = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)
	belong_to = fields.ForeignKey('wallet_wiki.resources.UserResource', 'belong_to', null=False, full=False)
	keyword   = fields.ToManyField('wallet_wiki.resources.KeywordResource', 'keyword', null=False, full=True)

	class Meta:
		resource_name		  = 'collection'
		queryset			   = Collection.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'belong_to': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()
		
	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<belong_to__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class CommentResource(ModelResource):
	author  = fields.ForeignKey('wallet_wiki.resources.UserResource', 'author', null=False, full=False)	
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name		  = 'comment'
		queryset			   = Comment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'article': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()

	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<article__id>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class AttachmentResource(ModelResource):
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name		  = 'attachment'
		queryset			   = Attachment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'article': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()

	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<article__id>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class MessageResource(ModelResource):
	from_user = fields.ToOneField('wallet_wiki.resources.UserResource', 'from_user', null=False, full=False)
	to_user = fields.ToOneField('wallet_wiki.resources.UserResource', 'to_user', null=False, full=False)

	class Meta:
		resource_name = 'message'
		queryset = Message.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'from_user': ALL_WITH_RELATIONS,
			'to_user': ALL_WITH_RELATIONS,
		}

	authentication = Authentication()
	authorization  = Authorization()

	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<from_user__user__username>[\w\d_.-]+)/(?P<to_user__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]



class FeedEventResource(ModelResource):
	article = fields.ToOneField('wallet_wiki.resources.ArticleResource', 'article', null=True, full=False)
	collection = fields.ToOneField('wallet_wiki.resources.CollectionResource', 'collection', null=True, full=False)
	inbox = fields.ToOneField('wallet_wiki.resources.InboxResource', 'inbox', null=False, full=True)
	
	class Meta:
		resource_name = 'feedevent'
		queryset = FeedEvent.objects.all()
		list_allowed_methods = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'inbox': ALL_WITH_RELATIONS,		
		}

	authentication = Authentication()
	authorization = Authorization()
	
	def override_urls(self):
		return [
			url(r"^(?P<resource_name>%s)/(?P<inbox__user__user__username>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_list'), name="api_dispatch_list"),
		]




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
