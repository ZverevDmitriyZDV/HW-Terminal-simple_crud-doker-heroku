FROM python:3.8
WORKDIR /simple_crud
COPY . .
RUN pip install -r requirements.txt
ENV PORT 8000
EXPOSE $PORT
#RUN python manage.py migrate
#RUN python manage.py colectstatic
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "collectstatic"]
CMD gunicorn -b 0.0.0.0:$PORT simple_crud.wsgi
