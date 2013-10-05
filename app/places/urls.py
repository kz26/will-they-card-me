from django.conf.urls import patterns, include, url
from app.places.views import *

urlpatterns = patterns('',
	url(r'^search/', Search.as_view(), name='places|search'),
)
