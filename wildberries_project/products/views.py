from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


from .models import Product
from .serializers import ProductSerializer, TaskIdSerializer
from .tasks import fetch_product_data
from django.shortcuts import get_object_or_404

@extend_schema(
    summary='Получение данных о товаре через API WB',
    description='Этот API позволяет получать информацию о товаре по его артикулу и токену. Используйте этот эндпоинт для асинхронного запроса данных о товаре из API Wildberries.'
)
class ProductView(APIView):
    # Добавляем сериализатор для корректного отображения схемы
    serializer_class = TaskIdSerializer

    def get(self, request, article, token):
        # Запуск асинхронной задачи через Celery
        task = fetch_product_data.delay(article, token)
        return Response({"task_id": task.id}, status=status.HTTP_202_ACCEPTED)




@extend_schema(
    summary='Получение списка товаров из нашей базы данных (т.е уже отобранных)',
    description='Используйте этот эндпоинт для отображения полученных товаров'
)
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'article'

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, article=kwargs.get('article'))
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)