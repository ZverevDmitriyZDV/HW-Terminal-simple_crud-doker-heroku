FROM python:3.8
WORKDIR /simple_crud
COPY . .
RUN pip install -r requirements.txt
CMD gunicorn simple_crud.wsgi -b 0.0.0.0:8000