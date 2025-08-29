FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:9000"]

# ENV PYTHONPATH=/app/app
# CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:9000"]
# CMD ["python", "app/manage.py", "runserver", "0.0.0.0:9000"]
