FROM python:3.6.3-slim

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]