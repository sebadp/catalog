"""
URL configuration for catalog_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from products.views import ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, BrandListCreateAPIView, \
    BrandRetrieveUpdateDestroyAPIView, CustomUserRetrieveUpdateDestroyAPIView, CustomUserListCreateAPIView

schema_view = get_schema_view(
    openapi.Info(
        #  add your swagger doc title
        title="Catalog API",
        #  version of the swagger doc
        default_version='v1',
        # first line that appears on the top of the doc
        description="Catalog API Documentation",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/users/', CustomUserListCreateAPIView.as_view(), name='user-list'),
    path('api/v1/users/<int:pk>/', CustomUserRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
    path('api/v1/products/', ProductListCreateAPIView.as_view(), name='product_list_create'),
    path('api/v1/products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_retrieve_update_destroy'),
    path('api/v1/brands/', BrandListCreateAPIView.as_view(), name='brand_list_create'),
    path('api/v1/brands/<int:pk>/', BrandRetrieveUpdateDestroyAPIView.as_view(),
         name='brand_retrieve_update_destroy'),

]