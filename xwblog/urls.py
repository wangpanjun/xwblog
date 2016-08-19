from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'xwblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^xwblog/', include('questions.urls')),
    url(r'^xwblog/', include('articles.urls')),
]
