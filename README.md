# Этот проект - тестовое задание по маркетплейсам.

# Описание:
API с двумя эндпоинтами:
1) Принимает на вход артикул товара Wildberries
2) Выводит список товаров с информацией о них.

# Технологии:

Python 3.10+, Django, DRF, PostgreSQL, Celery, Redis, Docker

# Для локальной загрузки требуется:
1. Загрузить приложение на ПК.
2. Установить виртуальное окружение с Python v3.10
3. Установить библиотеки. (в проекте использовался poetry)
   Для этого Вам нужно установить poetry - pip install poetry
   Затем для для установки всех библиотек  -   poetry install+
4. Теперь начинаем запускать проект. Вначале устанавливаем и запускаем сервер Redis для этого нужно воспользоваться официальной документацией https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
5. Теперь запускаем celery командой - celery -A wildberries_project worker -l info -P eventlet 
6. Теперь запускаем проект. Для запуска нужно запустить проект через manage.py  (python manage.py runserver)
  ( при запуске проекта в локальном виде  на адресе "0.0.0.0:8000"  нужно для входа использовать адрес "localhost:8000")
7. Для перехода к API переходим ао адресу http://localhost:8000/api/swagger 

   Дополнительно. Команда для запуска сайта на сервере или через Docker 
   
# Команда для запуска приложения через Docker
1. Для сбора и запуска контейнера используем команду docker-compose up --build

# This project is a test task on marketplaces.

# Description:
API with two endpoints:
1) Accepts the Wildberries product code as input
2) Displays a list of products with information about them.

# Technologies:

Python 3.10+, Django, DRF, PostgreSQL, Celery, Redis, Docker

# For local download you need:
1. Download the application to your PC.
2. Install a virtual environment with Python v3.10
3. Install libraries. (poetry was used in the project)
To do this, you need to install poetry - pip install poetry
Then to install all the libraries - poetry install+
4. Now we start running the project. First, install and run the Redis server. To do this, use the official documentation https://redis.io/docs/latest/operate/oss_and_stack/install/install-redis/install-redis-on-windows/
5. Now run celery with the command - celery -A wildberries_project worker -l info -P eventlet
6. Now run the project. To run, you need to run the project through manage.py (python manage.py runserver)
(when running the project locally at the address "0.0.0.0:8000", you need to use the address "localhost:8000" to log in)
7. To go to the API, go to the address http://localhost:8000/api/swagger

Additionally. Command to run the site on the server or via Docker

# Command to run the application via Docker
1. To build and run the container, use the docker-compose up --build command