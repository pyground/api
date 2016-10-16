FROM python:3.6

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "app/app.py"]
