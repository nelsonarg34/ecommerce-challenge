from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/user/', include('authentication.urls')),
    url(r'api/product/', include('product.urls')),
    url(r'api/order/', include('order.urls')),
    url(r'api/auth/obtain_token/', obtain_jwt_token),
    url(r'api/auth/refresh_token/', refresh_jwt_token),
]
