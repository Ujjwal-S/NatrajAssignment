from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('vehicle_app.urls')),
    path('', RedirectView.as_view(url='vehicles/')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)