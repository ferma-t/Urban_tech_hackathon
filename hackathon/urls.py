# -*- coding: utf-8 -*-
from datetime import datetime
from django.contrib import admin
from django.conf.urls import url,include
from django.conf.urls.static import static
from django.conf import settings
import django.contrib.auth.views
from hackathon.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/', include('hackathon.api.urls')),
    url(r'^accounts/', include('allauth.urls')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.UPLOAD_URL, document_root=settings.UPLOAD_ROOT)