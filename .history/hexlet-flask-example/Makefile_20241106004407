PORT ?= 8000

# Установить все зависимости и активировать виртуальное окружение без установки корневого пакета
install:
	poetry install --no-root

# Запустить приложение
run: install
	poetry run flask --app example/example.py --debug run --port $(PORT)

# Остановить приложение
stop:
	@echo "Остановить приложение: используйте Ctrl+C в окне с запущенным сервером"

# Проверить код, тесты и линтинг
test:
	poetry run pytest --cov=hexlet_flask_example

lint:
	poetry run flake8

check:	test lint
