
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('todos.urls', namespace='todos')),
    path('api/', include('api.urls', namespace='todos-api')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
