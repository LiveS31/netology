import os

CELERY_BROKER = os.getenv("CELERY_BROKER")
MONGO_DSN = os.getenv("MONGO_DSN")
PG_DSN = os.getenv("PG_DSN")
