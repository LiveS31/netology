import pymongo
from bson.objectid import ObjectId
from cachetools import cached
from celery import Celery
from celery.result import AsyncResult # для проверки состояния по id
from gridfs import GridFS

import face_checker
from config import CELERY_BROKER, MONGO_DSN, PG_DSN
#используем посгрес
celery_app = Celery("app", backend=f"db+{PG_DSN}", broker=CELERY_BROKER)


def get_task(task_id: str) -> AsyncResult:
    return AsyncResult(task_id, app=celery_app)


@cached({})
def get_fs():
    mongo = pymongo.MongoClient(MONGO_DSN)
    return GridFS(mongo["files"])


@celery_app.task
def match_photos(image_id_1, image_id_2):
    files = get_fs()
    return face_checker.match_photos(
        files.get(ObjectId(image_id_1)), files.get(ObjectId(image_id_2))
    )
