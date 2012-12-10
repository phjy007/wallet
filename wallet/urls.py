from django.conf.urls import patterns, include, url
from tastypie.api import Api
from wallet_wiki.resources import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(CategoryResource())
v1_api.register(KeywordResource())
v1_api.register(ArticleMetaResource())
v1_api.register(ArticleResource())
v1_api.register(CollectionResource())
v1_api.register(CommentResource())
v1_api.register(AttachmentResource())
v1_api.register(MessageResource())
v1_api.register(ArticleEventResource())
v1_api.register(CollectionEventResource())
v1_api.register(InboxResource())

# Just for test
# v1_api.register(TicketResource())
# v1_api.register(TicketCommentResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wallet.views.home', name='home'),
    # url(r'^wallet/', include('wallet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(v1_api.urls)),
)
