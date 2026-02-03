# backend_dite/urls.py (главный файл маршрутов проекта)
from django.contrib import admin
from django.urls import path, include, re_path # Убедитесь, что импортировали include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.views.generic import TemplateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/skills/", include("skills.urls")),
    re_path(r'^.*$', TemplateView.as_view(template_name="index.html")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)