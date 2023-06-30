from rest_framework import permissions
from rest_framework.permissions import BasePermission
#любой пермишен настледуется от базового класса

class IsAdvertisementOwner(BasePermission):
    #создаем свой класс
    def has_object_permission(self, request, view, obj):
        #проверяте права на конкретный объект
        # чтобы действие на чтение было доступно любому пользователю
        if request.method == 'GET':
            return True
        if request.user.is_superuser:
            return True
        return request.user == obj.creator
