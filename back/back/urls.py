from django.conf import settings
from django.conf.urls import url
from django.contrib import admin

from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter

from officialweb.views import upload_image
from officialweb import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'doc', views.DocViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}, ),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('docs/', include_docs_urls(title="许昌农商官网")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
]
