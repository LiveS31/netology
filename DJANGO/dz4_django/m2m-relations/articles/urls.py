from django.urls import path

from .views import articles_list

urlpatterns = [
    path('', articles_list, name='articles'),
]
