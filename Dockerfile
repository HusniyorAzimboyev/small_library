FROM python:3.11

WORKDIR /app

RUN apt-get update && apt-get install -y gcc

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]