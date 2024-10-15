import requests
from bs4 import BeautifulSoup
from celery import shared_task
from .models import Product


@shared_task
def fetch_product_data(article, token):

    headers = {"Authorization": f"Bearer {token}"}

    # URL для получения данных о товаре
    price_url = f"https://openapi.wildberries.ru/public/api/v1/info?quantity=1&nm={article}"
    # Получаем данные о товаре
    price_response = requests.get(price_url, headers=headers)
    if price_response.status_code == 200:
        price_data = price_response.json().get('data', {}).get('listGoods', [{}])[0]
    else:
        price_data = {}

    # URL для получения данных о складах
    stock_url = "https://openapi.wildberries.ru/statistics/api/v1/supplier/stocks"
    stock_response = requests.get(stock_url, params={"nm": article}, headers=headers)
    if stock_response.status_code == 200:
        stock_data = stock_response.json()
    else:
        stock_data = []

    # Сохраняем данные в базу данных или обновляем, если запись уже существует
    Product.objects.update_or_create(
        article=article,
        defaults={
            'name': price_data.get('vendorCode', 'Unknown'),
            'brand': price_data.get('brand', 'Unknown'),
            'price': price_data.get('priceU', 0) / 100,  # Цена делится на 100, так как она в API указана в копейках
            'discount': price_data.get('discount', 0),
            'stock_quantity': sum(item['quantity'] for item in stock_data),
            'warehouses': stock_data  # JSON с данными о складах
        }
    )
