# Game Web Service

## О проекте

Game Web Service - это веб-приложение, разработанное на Django, которое предоставляет API для игр. Этот проект включает базовую настройку и демонстрационные данные, чтобы начать разработку фронтенда.

## Требования

- Python 3.10 или выше ( в идеале актуальный 3.13)
- Poetry (для управления зависимостями и виртуальными окружениями)
- Git (для клонирования репозитория)

## Установка

### Шаг 1: Клонирование репозитория

Склонируйте репозиторий на ваш локальный компьютер:

```bash
git clone https://github.com/GeeksterVALO/Learning.git
cd GameWebService

#Шаг 2: Установка зависимостей
#Используйте Poetry для установки всех необходимых зависимостей:
bash
poetry install

#Шаг 3: Инициализация виртуального окружения
#Активируйте виртуальное окружение, созданное Poetry:
bash
poetry shell

#Шаг 4: Применение миграций базы данных
#Примените миграции базы данных, чтобы настроить схему базы данных:
bash
poetry run python manage.py migrate

#Шаг 5: Создание суперпользователя
#Создайте суперпользователя для доступа к административной панели Django:
bash
poetry run python manage.py createsuperuser

#Шаг 6: Запуск сервера разработки
#Запустите сервер разработки:
bash
poetry run python manage.py runserver
Откройте веб-браузер и перейдите по адресу http://127.0.0.1:8000, чтобы увидеть стартовую страницу проекта.
