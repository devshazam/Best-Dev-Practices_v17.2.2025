py -m pip install Django

django-admin startproject project

py manage.py startapp members

-> settings.py --> INSTALLED_APPS = [... <your_app_name>] 

python manage.py migrate

    py manage.py makemigrations members # после создания моделей

python manage.py runserver

