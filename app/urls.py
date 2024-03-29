from django.conf.urls import patterns, include, url
from django.views.generic import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^places/', include('app.places.urls')),
	url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
)
