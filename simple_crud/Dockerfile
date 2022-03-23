FROM python:3.8
WORKDIR /simple_crud
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python manage.py migrate
RUN python manage.py colectstatic
#CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "collectstatic"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "simple_crud.wsgi"]