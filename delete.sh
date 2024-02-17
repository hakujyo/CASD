#!/usr/bin/env sh

cd mysite || exit
rm -rf school/models.py
rm -rf school/serializers.py
rm -rf school/StudentViews.py

cp school/emptyurls.py school/urls.py

rm -rf school/migrations/*initial.py
rm -rf polls/migrations/*initial.py
rm db.sqlite3

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

