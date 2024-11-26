https://codante.io/testes-tecnicos/picpay

 - Atomicidade
    - garantir que as transações foram efetivadas em ambas as partes
 
 - bash
 - python3 -m venv venv
 - source venv/bin/activate
 - pip install django django-ninja django-role-permissions
 - django-admin startproject core .
 - python3 manage.py startapp users
 - python3 manage.py createsuperuser
 - pip install django.role-permissions
 - python3 manage.py startapp payments
 - pip install django-q
 - pip install --upgrade django-q
 - pip install "django<4.0"
 - python3 manage.py makemigrations
 - python3 manage.py migrate
 - python3 manage.py runserver
 - python3 manage.py qcluster