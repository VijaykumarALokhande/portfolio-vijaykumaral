from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import jobs.views
urlpatterns = [
    path('', jobs.views.home, name='homi'),
    path('admin/', admin.site.urls),
    path('BLogs/', include('temp.urls') ),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
