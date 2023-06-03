from django.urls import path
from .views import SensorView, SensorsView, MearsurementsView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MearsurementsView.as_view()),
]
