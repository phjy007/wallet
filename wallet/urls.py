from django.conf.urls import patterns, include, url
from tastypie.api import Api
from wallet_wiki.resources import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


v1_api = Api(api_name='v1')
v1_api.register(User_Resource())
v1_api.register(Category_Resource())
v1_api.register(Article_meta_Resource())
v1_api.register(Article_Resource())
v1_api.register(Keyword_Resource())

v1_api.register(TicketResource())
v1_api.register(TicketCommentResource())


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
