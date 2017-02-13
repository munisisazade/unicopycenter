"""Copycenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.utils import translation
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from center.views import delete_file
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^AJcrPnzDneoh/', delete_file ,name='delete'),
    url(r'^f4e6071b14b7.html$', TemplateView.as_view(template_name='f4e6071b14b7.html')),
    url(r'^google71597c4e3ad7b723.html$', TemplateView.as_view(template_name='google71597c4e3ad7b723.html')),
    url(r'^favicon.ico$', TemplateView.as_view(template_name='favicon.ico',context_type="image/x-icon")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += i18n_patterns(
    url(r'^', include('center.urls')),
)