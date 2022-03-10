FROM python:3.8
WORKDIR /simple_crud
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "simple_crud.wsgi"]