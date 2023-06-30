from rest_framework.permissions import BasePermission
#любой пермишен наследуется от базового класса

class IsOwnerOrReadOnly(BasePermission):# создаем свой класс

    # создаем первую функцию - имеет ли пользователь право
    # на работу с ресурсом в целом.
    #def has_permission(self, request, view):#по-умолчанию значение
        # True (имеет). Но нужен другой
    def has_object_permission(self, request, view, obj):# проверяет права
        # на конкретный объект
# чтобы действие на чтение было доступно любому пользователю
        # нужно добавить следующий функционал
        if request.method == 'GET':# если действие запроса
            return True # всегда возвращать True
        return request.user == obj.user# возвращаем статус (True) совпадает
        # или нет пользователь сообщения с пользователем из запроса