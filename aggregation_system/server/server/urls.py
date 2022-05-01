from django.contrib import admin
from django.urls import path
from django.urls.conf import include

"""
    Main links for api
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web_client.urls')),
    path('test-server/', include('test_server.urls'))
]
