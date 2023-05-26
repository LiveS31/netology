from django.views.generic import ListView
from django.shortcuts import render

from .models import Student, Teacher

def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all().\
        order_by('group').prefetch_related('teachers')
    context = {'students': students}
    #context = {'object_list': students,
               #'teachers': Teacher.objects.all()}
    #ordering = 'group'
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by


    return render(request, template, context)