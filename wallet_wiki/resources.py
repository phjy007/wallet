from django.db import models
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.authentication import Authentication,BasicAuthentication
from tastypie.authorization import Authorization, DjangoAuthorization
from tastypie import fields
from wallet_wiki.models import *


class User_Resource(ModelResource):
	class Meta:
		resource_name          = 'user'
		queryset               = UserProfile.objects.all()
		list_allowed_methods   = ['get', 'post']	
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		excludes               = ['password']
		filtering = {
			'username': ('exact', ),
			'nickname': ('exact', ),
			'email': ('exact', ),
		}
		authentication = Authentication()
		authentication = Authorization()



class Inbox_Resource(ModelResource):
	pass



class Inbox_item_Resource(ModelResource):
	pass



class Category_Resource(ModelResource):
	parent_category = fields.ForeignKey('wallet_wiki.resources.Category_Resource', 'parent_category')

	# def dehydrate(self, bundle):
	# 	sons = Category.objects.filter(category_name=bundle.data['category_name'])
	# 	bundle.data['sons'] = [model_to_dict(c) for c in sons]
	# 	return bundle

	# def dehydrate_category_name(self, bundle):
	# 	return bundle.data['category_name'].upper()

	class Meta:
		resource_name          = 'category'
		queryset               = Category.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'category_name': ('exact', ),
		}

	authentication = Authentication()
	authentication = Authorization()



class Keyword_Resource(ModelResource):
	author = fields.ForeignKey('wallet_wiki.resources.User_Resource', 'author')

	class Meta:
		resource_name          = 'keyword'
		queryset               = Keyword.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']
		filtering = {
			'keyword_name': ('exact', ),
		}

	authentication = Authentication()
	authentication = Authorization()



class Article_meta_Resource(ModelResource):
	category = fields.ToManyField('wallet_wiki.resources.Category_Resource', 'category')
	# keyword = fields.ToManyField('wallet_wiki.resources.Keyword_Resource', 'article_meta_keyword')
	sited_article = fields.ToManyField('wallet_wiki.resources.Article_meta_Resource', 'article_meta_sited_article', full=True)
	siting_article = fields.ToManyField('wallet_wiki.resources.Article_meta_Resource', 'article_meta_siting_article', full=True)

	class Meta:
		resource_name          = 'article_meta'
		queryset               = Article_meta.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authentication = Authorization()
		



class Article_Resource(ModelResource):
	meta = fields.ForeignKey('wallet_wiki.resources.Article_meta_Resource', 'meta', full=True)

	class Meta:
		resource_name          = 'article'
		queryset               = Article.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authentication = Authorization()
		


class Draft_Resource(ModelResource):
	pass



class Collection_Resource(ModelResource):
	pass



class Comment_Resource(ModelResource):
	pass



class Attachment_Resource(ModelResource):
	pass



class Message_Resource(ModelResource):
	pass





#Just for test
class TicketResource(ModelResource):

    class Meta:
        queryset = Ticket.objects.all()
        resource_name = 'ticket'

    def dehydrate(self, bundle):
        comments = TicketComment.objects.filter(ticket=bundle.data['id'])
        bundle.data['comments'] = [model_to_dict(c) for c in comments]
        # print '\n@#>> ', bundle, '\n**&*\n'
        return bundle

class TicketCommentResource(ModelResource):
    ticket = fields.ForeignKey(TicketResource, 'ticket', full=True)

    class Meta:
        queryset = TicketComment.objects.all()
        resource_name = 'comment'
