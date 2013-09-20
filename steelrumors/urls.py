from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from links.views import LinkListView

urlpatterns = patterns('',
url(r'^$', LinkListView.as_view(), name='home'),

    # Examples:
    # url(r'^$', 'steelrumors.views.home', name='home'),
    # url(r'^steelrumors/', include('steelrumors.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
