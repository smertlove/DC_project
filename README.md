# Установка виртуального окружения и зависимостей:
* `...\> python -m venv env`
* `...\> env\Scripts\activate`
* `(env) ...\> pip install -r requirements.txt`

# Не забываем провести миграции при первом запуске:
* `(env) ...\> cd my_site`
* `(env) ...\> python manage.py makemigrations`
* `(env) ...\> python manage.py migrate`

# КАЖДЫЙ РАЗ КОГДА ДОБАВЛЯЕМ ЗАВИСИМОСТЬ:
* `(env) ...\> pip freeze > requirements.txt` из корня проекта.
