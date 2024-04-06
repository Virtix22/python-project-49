install:
	poetry install #Установка пакета

brain-games:
	poetry run brain-games #Запуск программы

build:
	poetry build #Сборка дистрибутива пакета с помощью Poetry

publish:
	poetry publish --dry-run #Публикация пакетов Python в PyPI

package-install:
	python3 -m pip install --user dist/*.whl #Установка программы

lint:
	poetry run flake8 brain_games #запуск линтера для проверки чистоты кода
