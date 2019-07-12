from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from uploads.core import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    path('filter/<str:val>/', views.cat, name='cat'),
    url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
    path('uploads/<int:pk>/', views.donate_item, name='donate_item'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
