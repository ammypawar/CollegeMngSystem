from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = patterns('',
    # Enable the URLs when implemented
    url(r'^admin/', include(admin.site.urls)),
    url(r'^administrator/', include('administrator.urls', namespace='cms-admin')),
    
)