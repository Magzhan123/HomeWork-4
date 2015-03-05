from django.conf.urls import patterns, url

from blogApp import views
#from magzhan.blogApp.api import Post
urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<blog_id>\d+)/$', views.postShow, name='blog'),
    # ex: /polls/5/results/
)