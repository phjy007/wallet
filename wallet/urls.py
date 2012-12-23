from django.conf.urls import patterns, include, url
from tastypie.api import Api
from wallet_wiki.resources import *
from wallet_wiki.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UserCoreResource())
v1_api.register(CategoryResource())
v1_api.register(KeywordResource())
v1_api.register(ArticleMetaResource())
v1_api.register(ArticleResource())
v1_api.register(CollectionResource())
v1_api.register(CommentResource())
v1_api.register(AttachmentResource())
v1_api.register(MessageResource())
v1_api.register(FeedEventResource())
# v1_api.register(ArticleEventResource())
# v1_api.register(CollectionEventResource())
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

    url(r'^login/', login_view),
    url(r'^logout/', logout_view),

	url(r'^index/', show_index),

	url(r'^homepage/(\w+)/$', show_homepage), # when someone login successfully, this url takes him to his own homepage
    url(r'^homepage/(\w+)/new_article/$', write_new_article), # the page that user can write a new article
    url(r'^homepage/(\w+)/my_article/(\d+)/$', show_my_article), # the page that user can write a new article

    url(r'^/piggybank/(\w+)/article/(\d+)/$', view_article), # view other's article
    url(r'^/piggybank/(\w+)/$', visit_someone_piggybank),  # view other's page
)
