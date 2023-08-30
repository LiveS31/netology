FROM python:3.10

WORKDIR /docker

COPY . .

RUN pip3 install --no-cache-dir --upgrade -r /docker/requirements.txt

EXPOSE 80

CMD gunicorn stocks_products/stocks_products.wsgi -b 0.0.0.0:80
