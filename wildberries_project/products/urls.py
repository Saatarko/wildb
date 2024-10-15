from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from rest_framework.routers import DefaultRouter

from .views import ProductView, ProductDetailView


urlpatterns = [

    path('получение-товара с API WB/<str:article>/<str:token>/', ProductView.as_view(), name="product_view"),  # <-- стандартный путь для классов
    path('Выдача данных из базы/', ProductDetailView.as_view(), name="product-fetch"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]