from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from students.filters import CourseFilter
from students.models import Course, Student #из каких таблиц берем данные
#соответственно импортируем

#снова импортируем
from students.serializers import CourseSerializer, StudentSerializer



class CoursesViewSet(ModelViewSet):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = CourseFilter

# создаем класс студент и наслеуем его
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all() # откуда берем данные и какие
    serializer_class = StudentSerializer # создаем Serializer для передачи по API
