from django.conf.url import pattern, url
from rango import index

urlpatterns = pattern('',
	url(r'^$', rango.index, name="index")) 