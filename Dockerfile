FROM python:3.10.11

RUN git clone https://github.com/lhjwork/pinterest_django.git

WORKDIR /home/

WORKDIR /home/pinterest_django/

RUN python3 -m venv /myvenv

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-fwei5h(cgr6%5i4ipaiv%g7_mzes%u1ge9)3*di^mm%-e^!1+*" > .env

RUN python3 manage.py migrate

EXPOSE 8000

CMD ["gunicorn","pinterest_django.wsgi", "--bind", "0.0.0.0:8000"]