from django.conf.urls import re_path, include
from django.contrib import admin

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^api/', include('shop.urls')),
    re_path(r'^api/', include('common.urls')),
    
]
