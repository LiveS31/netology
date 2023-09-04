FROM python:3.10

WORKDIR /app

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["sh", "-c", "python manage.py collectstatic --no-input && python manage.py migrate"]
