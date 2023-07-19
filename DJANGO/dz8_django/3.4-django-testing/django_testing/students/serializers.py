from rest_framework import serializers

from students.models import Course, Student


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ("id", "name", "students")
# создаем StudentSerialiazer для передачи по API
# Наследуем его от высшего класса
class StudentSerializer(serializers.ModelSerializer):
    class Meta: # пишем дополнительную инфу
        model = Student #импортируем из модели
        fields = ('id', 'name', 'birth_date')

    def validate(self, attrs): # используем несколько полей
        student_count = Student.objects.count() #количество запросов
        if student_count >= 20: #условие уведомления
            #оно самое
            raise serializers.ValidationError('Достигнуто максимальное значение 20')
        return attrs #возврат при ок
