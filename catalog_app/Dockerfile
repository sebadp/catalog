FROM python:3

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE settings.local

WORKDIR /usr/src/app

COPY ./catalog_app /usr/src/app/

RUN pip3 install requirements.txt

RUN python3 manage.py migrate

RUN python3 manage.py runserver 0.0.0.0:8000


