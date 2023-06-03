# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from .serializers import SensorSerializer, SensorDetailSerializer, MeasuremetDetailSerializer
from .models import Sensor, Measurement

class SensorsView(ListAPIView): #для чтения конечных точек (через get)
    queryset = Sensor.objects.all() #обращаемся к классу
    serializer_class = SensorSerializer # отображаем через это

    def post(self, request):
        Sensor.objects.create(      #создаем записи в базе данных
            name=request.POST.get('name'),
            descripcion=request.POST.get('description')
        )
        return ({'status':'Ok'})    #выводим статус

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk): #вносим данные со связкой и сохраняем
        sensor = Sensor.objects.get(id=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'Status':'Ok'})

class MearsurementsView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasuremetDetailSerializer

    def post(self, request):
        Measurement.objects.create(
            sensor_id=request.POST.get('sensor'),
            temperature=request.POST.get('temperature')
        )
        return Response({'status':'Ok'})