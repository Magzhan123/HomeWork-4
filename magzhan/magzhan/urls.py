from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogApp.api import PostResource
from blogApp.api import CommentResource
post_resource = PostResource()
comment_resource = CommentResource()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'magzhan.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blogApp/', include('blogApp.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(post_resource.urls)),
    url(r'^api/v1/', include(comment_resource.urls)),
)
