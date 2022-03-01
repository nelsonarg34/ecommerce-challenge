from django.contrib import admin

from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('authentication.urls')),
    path('api/product/', include('product.urls')),
    path('api/order/', include('order.urls')),
    
]
