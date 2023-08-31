FROM python:3.10

WORKDIR /app

COPY . .
COPY nginx.conf /etc/nginx/nginx.conf
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
#RUN --name my-custom-nginx-container -v /host/path/nginx.conf:/etc/nginx/nginx.conf:ro -d nginx

CMD ["sh", "-c", "python3 manage.py collectstatic --no-input && python3 manage.py migrate"]
