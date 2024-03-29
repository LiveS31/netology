import uuid
import os

from flask import Flask
from flask import request
from flask.views import MethodView
from flask import jsonify
from celery import Celery
from celery.result import AsyncResult

from face_checker import FaceChecker



app_name = 'app'
app = Flask(app_name)
app.config['UPLOAD_FOLDER'] = 'files'
celery = Celery(
    app_name,
    backend='redis://localhost:6379/3',
    broker='redis://localhost:6379/4'
)
celery.conf.update(app.config)


########################################################
#### данная конструкция позволяет правильно работать с flask
class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask
###########################################################

@celery.task()
def match_photos(path_1, path_2):
#принимает два пути к фотографиям
    result = FaceChecker.with_files().match(path_1, path_2)
#применяет пути распознавания лиц
    return result


class Comparison(MethodView):

    def get(self, task_id): # будем доставать задачу через task_id
        task = AsyncResult(task_id, app=celery) # доставать будем из редиса
        return jsonify({'status': task.status, # скидываем клиенту статус
                        'result': task.result}) # скидываем результат

    def post(self): # поступают две фотографии
        # в полях image_1/image_2
        image_pathes = [self.save_image(field) for field in ('image_1', 'image_2')]
        #фото сохраняются на диск через функцию - seif_image
        task = match_photos.delay(*image_pathes)
        return jsonify( #возвращается id созданной задачи
            {'task_id': task.id}
        )

    def save_image(self, field):
        image = request.files.get(field)
        extension = image.filename.split('.')[-1]
        path = os.path.join('files', f'{uuid.uuid4()}.{extension}')
        image.save(path)
        return path

#методы get и post - их привязка к url (class Comparison(MethodView))
comparison_view = Comparison.as_view('comparison')
app.add_url_rule('/comparison/<string:task_id>', view_func=comparison_view, methods=['GET'])
app.add_url_rule('/comparison/', view_func=comparison_view, methods=['POST'])


if __name__ == '__main__':
    app.run()
