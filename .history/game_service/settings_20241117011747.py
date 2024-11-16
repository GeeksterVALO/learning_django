import os
from pathlib import Path

# Объяснение:
# Базовая директория проекта: Определяет корневую директорию проекта.
# Секретный ключ: Используется для криптографических подписей.
# Режим отладки: Включает/выключает режим отладки.
# Разрешенные хосты: Список хостов, которым разрешено подключаться к проекту.
# Приложения Django: Список установленных приложений.
# Промежуточное ПО (middleware): Список промежуточного ПО.
# URL конфигурация: Определяет корневой URL конфигурации.
# Шаблоны: Настройки шаблонов.
# WSGI приложение: Определяет WSGI приложение.
# База данных: Настройки базы данных.
# Валидаторы паролей: Список валидаторов паролей.
# Интернационализация: Настройки языка и часового пояса.
# Статические файлы: Настройки для статических файлов.
# Медиа файлы: Настройки для загружаемых пользователями файлов.
# Тип поля по умолчанию для первичных ключей: Определяет тип поля по умолчанию для первичных ключей.
# Кастомная модель пользователя: Указывает на кастомную модель пользователя.


# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ для криптографических подписей
SECRET_KEY = 'your-secret-key'

# Режим отладки (не включайте в продакшн)
DEBUG = True

# Разрешенные хосты
ALLOWED_HOSTS = []

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'games',
    'news',
    'catalog',
]

# Промежуточное ПО (middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL конфигурация
ROOT_URLCONF = 'game_service.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI приложение
WSGI_APPLICATION = 'game_service.wsgi.application'

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валидаторы паролей
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Интернационализация
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Медиа файлы (загружаемые пользователями файлы)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Тип поля по умолчанию для первичных ключей
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Кастомная модель пользователя
AUTH_USER_MODEL = 'users.User'



