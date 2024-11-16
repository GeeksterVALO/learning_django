## Установка

## Требования

- Python 3.13
- pip
- Poetry
- Git

### 1. Клонирование репозитория

#Склонируйте репозиторий на ваш локальный компьютер:

```sh
git clone https://github.com/GeeksterVALO/Learning.git
cd Learning

#Если у вас еще не установлен Poetry, установите его:
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -

#Создание и активация виртуального окружения
poetry shell

#Установите зависимости проекта с помощью Poetry:
poetry install

##Примените миграции базы данных:
poetry run python manage.py makemigrations
poetry run python manage.py migrate

#Создание суперпользователя
poetry run python manage.py createsuperuser

#Запустите сервер разработки:
poetry run python manage.py runserver