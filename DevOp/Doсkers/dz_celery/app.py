import cv2
from celery import Celery
from celery.result import AsyncResult
from cv2 import dnn_superres
from flask import Flask, jsonify, request, send_from_directory
from flask.views import MethodView

app_name = "app"
app = Flask(app_name)
app.config["UPLOAD_FOLDER"] = "files"
celery = Celery(
    app_name, backend="redis://localhost:6379/3", broker="redis://localhost:6379/4"
)
celery.conf.update(app.config)


class ContextTask(celery.Task):
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return self.run(*args, **kwargs)

celery.Task = ContextTask



def load_scaler(model_path: str = "upscale/EDSR_x2.pb"):
    scaler = dnn_superres.DnnSuperResImpl_create()
    scaler.readModel(model_path)
    scaler.setModel("edsr", 2)
    return scaler
scaler = load_scaler()


@celery.task()
def upscale(input_path: str, output_path: str) -> str:
    """
    :param input_path: путь к изображению для апскейла
    :param output_path:  путь к выходному файлу
    :return: output_path
    """
    img = cv2.imread(input_path)
    result = scaler.upsample(img)
    cv2.imwrite(output_path, result)
    return output_path


class UpscaleView(MethodView):
    def get(self, task_id):
        task = AsyncResult(task_id, app=celery)
        if task.status == "SUCCESS":
            result_link = f"{request.host_url}{task.result}"
            return jsonify({"status": task.status, "result_link": result_link})
        else:
            return jsonify({"status": task.status, "result_link": None})

    def post(self):
        input_file = "files/lama_300px.png"
        output_file = "files/lama_600px.png"
        task = upscale.delay(input_file, output_file)
        return jsonify(
            {
                "task_id": task.id,
            }
        )


def download(file):
    return send_from_directory(app.config["UPLOAD_FOLDER"], file)


upscale_view = UpscaleView.as_view("upscale")
app.add_url_rule("/tasks/<string:task_id>/", view_func=upscale_view, methods=["GET"])
app.add_url_rule("/processed/<string:file>/", view_func=download, methods=["GET"])
app.add_url_rule("/upscale/", view_func=upscale_view, methods=["POST"])


if __name__ == "__main__":
    app.run()