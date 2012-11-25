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
		authentication = Authorization()

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



class InboxItemResource(ModelResource):
	pass



class CategoryResource(ModelResource):
	parent_category = fields.ForeignKey('self', 'parent', null=True, full=True)

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



class KeywordResource(ModelResource):
	# author = fields.ForeignKey('wallet_wiki.resources.User_Resource', 'author')

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



class ArticleMetaResource(ModelResource):
	category = fields.ToManyField('wallet_wiki.resources.Category_Resource', 'category')
	keyword = fields.ToManyField('wallet_wiki.resources.Keyword_Resource', 'article_meta_keyword')
	# sited_article = fields.ToManyField('wallet_wiki.resources.Article_meta_Resource', 'article_meta_sited_article', full=True)
	siting_article = fields.ToManyField('wallet_wiki.resources.Article_meta_Resource', 'article_meta_siting_article', full=True)

	class Meta:
		resource_name          = 'article_meta'
		queryset               = ArticleMeta.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authentication = Authorization()
		



class ArticleResource(ModelResource):
	meta = fields.ForeignKey('wallet_wiki.resources.Article_meta_Resource', 'meta', full=True)

	class Meta:
		resource_name          = 'article'
		queryset               = Article.objects.all()
		list_allowed_methods   = ['get', 'post']
		detail_allowed_methods = ['get', 'post', 'put', 'delete']

	authentication = Authentication()
	authentication = Authorization()
		


class DraftResource(ModelResource):
	pass



class CollectionResource(ModelResource):
	pass



class CommentResource(ModelResource):
	pass



class AttachmentResource(ModelResource):
	pass



class MessageResource(ModelResource):
	pass





#Just for test
class TicketResource(ModelResource):

    class Meta:
        queryset = Ticket.objects.all()
        resource_name = 'ticket'

    def dehydrate(self, bundle):
        comments = TicketComment.objects.filter(ticket=bundle.data['id'])
        bundle.data['comments'] = [model_to_dict(c) for c in comments]
        return bundle

class TicketCommentResource(ModelResource):
    ticket = fields.ForeignKey(TicketResource, 'ticket', full=True)

    class Meta:
        queryset = TicketComment.objects.all()
        resource_name = 'comment'
