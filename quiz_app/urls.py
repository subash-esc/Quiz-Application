from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^select/', views.select, name='select'),
    url(r'^play/', views.play, name='play'),
    url(r'^rule/', views.rule, name='rule'),
    url(r'^result/', views.result, name='result'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)