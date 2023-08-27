FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip

RUN  pip install --upgrade setuptools

RUN pip install -r requirements.txt

CMD ["./docker/python/wait-for-it.sh", "db:3306", "--", "gunicorn", "--bind", "0.0.0.0:8000", "news_portal.wsgi"]

