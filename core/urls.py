from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/user/', include('authentication.urls')),
    url(r'api/product/', include('product.urls')),
]
