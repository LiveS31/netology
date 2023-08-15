from django.urls import path

from .views import articles_list, test_page

urlpatterns = [
    path('', articles_list, name='articles'),
    path('1',test_page, name='test' ),
]
