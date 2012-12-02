from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication, BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields
from wallet_wiki.models import *


class UserResource(ModelResource):
	following = fields.ToManyField('self', 'following', null=True)

	class Meta:
		resource_name          = 'user'
		queryset               = UserProfile.objects.all()
		list_allowed_methods   = ['get', 'post']	
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		excludes               = ['password', 'date_joined', 'is_active', 'is_staff', 'last_login', 'first_name', 'last_name']
		filtering = {
			'username': ('exact', ),
			'nickname': ('exact', ),
			'email': ('exact', ),
		}
		authentication = BasicAuthentication()
		authorization  = DjangoAuthorization()

	def dehydrate(self, bundle):
		this = UserProfile.objects.get(id=bundle.data['id'])
		fans = this.userprofile_set.all()
		if fans is not None:
			bundle.data['fans'] = []
			for c in fans:
				bundle.data['fans'].append(c.get_absolute_url())
		else:
			bundle.data['fans'] = 'None'
		return bundle	




class InboxResource(ModelResource):
	pass




class CategoryResource(ModelResource):
	parent_category = fields.ForeignKey('self', 'parent', null=True, full=True)

	class Meta:
		resource_name          = 'category'
		queryset               = Category.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'category_name': ('exact', ),
		}

	authentication = Authentication()
	authorization  = Authorization()

	# def dehydrate(self, bundle):
	# 	# GET A CATEGORY'S SONS! ******************************************
	# 	# sons = Category.objects.filter(parent=bundle.data['id'])
	# 	# bundle.data['sons'] = [model_to_dict(c) for c in sons]
	# 	# for c in sons:
	# 	# 	print c
	# 	# GET A CATEGORY'S PARENT *****************************************
	# 	this = Category.objects.get(id=bundle.data['id'])
	# 	p = this.parent
	# 	print p	
	# 	if p is not None:
	# 		bundle.data['parent'] = model_to_dict(p)
	# 	else:
	# 		bundle.data['parent'] = 'None'
	# 	return bundle

	# def dehydrate_category_name(self, bundle):
	# 	return bundle.data['category_name'].upper()



class KeywordResource(ModelResource):
	keyword_author = fields.ToOneField('wallet_wiki.resources.UserResource', 'author', null=False, full=True)

	class Meta:
		resource_name          = 'keyword'
		queryset               = Keyword.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'keyword_name': ('exact', ),
		}

	authentication = Authentication()
	authorization  = Authorization()



class ArticleMetaResource(ModelResource):
	category       = fields.ToManyField('wallet_wiki.resources.CategoryResource', 'category', null=True, full=False)
	keyword        = fields.ToManyField('wallet_wiki.resources.KeywordResource', 'keyword', null=True, full=False)
	siting_article = fields.ToManyField('wallet_wiki.resources.ArticleMetaResource', 'siting_article', null=False, full=False)
	author         = fields.ForeignKey('wallet_wiki.resources.UserResource', 'author', null=False, full=False)

	class Meta:
		resource_name          = 'article_meta'
		queryset               = ArticleMeta.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()
		
	def dehydrate(self, bundle):
		this = ArticleMeta.objects.get(id=bundle.data['id'])
		# get articles belonging to this article meta
		versions = this.article_set.all()
		if versions is not None:
			bundle.data['versions'] = []
			for c in versions:
				bundle.data['versions'].append(c.get_absolute_url())
		else:
			bundle.data['versions'] = 'None'
		# get sited articles
		sited_articles = this.articlemeta_set.all()
		if sited_articles is not None:
			bundle.data['sited_articles'] = []
			for c in sited_articles:
				bundle.data['sited_articles'].append(c.get_absolute_url())
		else:
			bundle.data['sited_articles'] = 'None'
		return bundle	



class ArticleResource(ModelResource):
	meta = fields.ForeignKey('wallet_wiki.resources.ArticleMetaResource', 'meta', null=False, full=False)

	class Meta:
		resource_name          = 'article'
		queryset               = Article.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	def dehydrate(self, bundle):
		this = Article.objects.get(id=bundle.data['id'])
		comments = this.comment_set.all()
		if comments is not None:
			bundle.data['comments'] = []
			for c in comments:
				bundle.data['comments'].append(c.get_absolute_url())
		else:
			bundle.data['comments'] = 'None'
		return bundle

	authentication = Authentication()
	authorization  = Authorization()
		



class CollectionResource(ModelResource):
	meta      = fields.ForeignKey('wallet_wiki.resources.ArticleMetaResource', 'article_meta', null=False, full=True)
	belong_to = fields.ForeignKey('wallet_wiki.resources.UserResource', 'belong_to', null=False, full=True)
	keyword   = fields.ToManyField('wallet_wiki.resources.KeywordResource', 'keyword', null=False, full=True)

	class Meta:
		resource_name          = 'collection'
		queryset               = Collection.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()
		


class CommentResource(ModelResource):
	author  = fields.ForeignKey('wallet_wiki.resources.UserResource', 'author', null=False, full=False)	
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name          = 'comment'
		queryset               = Comment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()



class AttachmentResource(ModelResource):
	article = fields.ForeignKey('wallet_wiki.resources.ArticleResource', 'article', null=False, full=False)

	class Meta:
		resource_name          = 'attachment'
		queryset               = Attachment.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authorization  = Authorization()



class MessageResource(ModelResource):
	pass




class ArticleEventResource(ModelResource):
	pass






#Just for test
# class TicketResource(ModelResource):

#     class Meta:
#         queryset = Ticket.objects.all()
#         resource_name = 'sample_ticket'

#     def dehydrate(self, bundle):
#         comments = TicketComment.objects.filter(ticket=bundle.data['id'])
#         bundle.data['comments'] = [model_to_dict(c) for c in comments]
#         return bundle

# class TicketCommentResource(ModelResource):
#     ticket = fields.ForeignKey(TicketResource, 'ticket', full=True)

#     class Meta:
#         queryset = TicketComment.objects.all()
#         resource_name = 'sample_comment'
