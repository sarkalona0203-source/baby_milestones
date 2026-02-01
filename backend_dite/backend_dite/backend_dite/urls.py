# backend_dite/urls.py (главный файл маршрутов проекта)
from django.contrib import admin
from django.urls import path, include  # Убедитесь, что импортировали include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

def home(request):
    return HttpResponse("Backend 🚀")
urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api/skills/', include('skills.urls')),  # Подключаем urls вашего приложения
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)