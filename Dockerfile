FROM python:3.10.11

WORKDIR /home/

RUN git clone https://github.com/lhjwork/pinterest_django.git

WORKDIR /home/pinterest_django/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-fwei5h(cgr6%5i4ipaiv%g7_mzes%u1ge9)3*di^mm%-e^!1+*" > .env

RUN python3 manage.py migrate

EXPOSE 8000

CMD ["gunicorn","pragmatic.wsgi", "--bind", "0.0.0.0:8000"]

#http://158.247.240.178:8080/