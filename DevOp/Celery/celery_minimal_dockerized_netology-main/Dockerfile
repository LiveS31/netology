FROM python:3.10
COPY ./ /app
WORKDIR /app
RUN pip install --no-cache-dir -r /app/requirements.txt
ENV PYTHONUNBUFFERED=TRUE
