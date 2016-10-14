from django.conf.urls import include, url
from django.contrib import admin

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'xwblog.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^$', 'index.views.index'),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^xwblog/', include('questions.urls')),
#     url(r'^xwblog/', include('articles.urls')),
# ]
from labels.apis import LabelsViewSet, LabelViewSet

from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'labels', LabelsViewSet, base_name='labels')
router.register(r'label', LabelViewSet, base_name='label')

urlpatterns = router.urls
urlpatterns += [
    # Examples:
    # url(r'^$', 'restdemo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # /api-auth/  for session authentication page, If you're intending to use
    # the browsable API, or you want allow only authenticated user to access
    # the rest api, you'll probably also want to add REST framework's login and logout views.
    # If you allow anonymous access in rest permission, wont need the mapping.
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', views.obtain_auth_token),  ## token auth
    url(r'^api-token-auth/', 'users.views.obtain_expiring_auth_token'),  ## token auth
]
