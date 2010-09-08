from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^(?P<shortname>\w+)', 'armchairs.shorturls.views.index'),
)
