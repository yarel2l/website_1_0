"""website_1_0 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/{{ docs_version }}/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [

    url(r'^$', views.Homepage.as_view(), name = 'homepage'),
    # url(r'^blog/', include('blog.urls'), name = 'blog'),
    # url(r'^settings/', include('configuration.urls'), name = 'configuration'),
    url(r'^services/', include('services.urls', namespace = 'services')),
    url(r'^portfolio/', include('portfolio.urls', namespace = 'portfolio')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_URL)
