FROM python:3.10

WORKDIR /app

COPY . .
COPY stocks_products/nginx/nginx.conf /etc/nginx/nginx.conf
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["sh", "-c", "python manage.py collectstatic --no-input && python manage.py migrate"]
