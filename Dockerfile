FROM python:3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.pip ./

RUN pip install -r requirements.pip

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]