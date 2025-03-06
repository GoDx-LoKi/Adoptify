from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from django.contrib import admin
from django.urls import path, include
from pages.views import home  # Import the home view

from pages.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('pets/', include('pets.urls')),
    path('accounts/', include('accounts.urls')),
    path('inquiries/', include('inquiries.urls')),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('donation/', TemplateView.as_view(template_name='donation.html'), name='donation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

