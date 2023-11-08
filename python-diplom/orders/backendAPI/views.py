from distutils.util import strtobool

from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.db import IntegrityError
from django.db.models import Q, Sum, Prefetch
from requests import get
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from yaml import load as load_yaml, Loader
from ujson import loads as load_json
from .serializers import UserSerializer, ContactSerializer, ShopSerializer, CategorySerializer, \
    ProductSerializer, OrderSerializer, OrderItemAddSerializer
from .models import ConfirmEmailToken, Contact, Shop, Category, Product, Order, OrderItem

# e8c8510b04c39d49f7475dc46605cecbf40ea9ff63f


class RegisterUser(APIView):
    '''
    Регистрация покупателя
    '''
    throttle_scope = 'register'

    def post(self, request, *args, **kwargs):
        if {'first_name', 'last_name', 'email', 'password', 'company', 'position'}.issubset(request.data):
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                return Response({'status': False, 'error': {'password': password_error}},
                                status=status.HTTP_403_FORBIDDEN)
            else:
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user = user_serializer.save()
                    user.set_password(request.data['password'])
                    user.save()
                    token, _ = ConfirmEmailToken.objects.get_or_create(user_id=user.id)
                    return Response({'status': True, 'token for confirm email': token.key})
                else:
                    return Response({'status': False, 'error': user_serializer.errors},
                                    status=status.HTTP_403_FORBIDDEN)
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class ConfirmAccount(APIView):
    """
    Подтверждение регистрации
    """
    # Регистрация методом POST
    def post(self, request, *args, **kwargs):

        # проверяем обязательные аргументы
        if {'email', 'token'}.issubset(request.data):

            token = ConfirmEmailToken.objects.filter(user__email=request.data['email'],
                                                     key=request.data['token']).first()
            if token:
                token.user.is_active = True
                token.user.save()
                token.delete()
                return Response({'Status': True})
            else:
                return Response({'Status': False, 'Errors': 'Неправильно указан токен или email'})

        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

class LoginUser(APIView):
    '''
    Авторизация
    '''
    def post(self, request, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])
            if user is not None:
                if user.is_active:
                    token, _ = Token.objects.get_or_create(user=user)

                    return Response({'status': True, 'token': token.key})

            return Response({'status': False, 'error': 'Не удалось войти'}, status=status.HTTP_403_FORBIDDEN)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class UserDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        возвращает все данные пользователя
        '''
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        Изменения данных пользователя
        '''
        if {'password'}.issubset(request.data):
            if 'password' in request.data:
                try:
                    validate_password(request.data['password'])
                except Exception as password_error:
                    return Response({'status': False, 'error': {'password': password_error}},
                                    status=status.HTTP_400_BAD_REQUEST)
                else:
                    request.user.set_password(request.data['password'])

            user_serializer = UserSerializer(request.user, data=request.data, partial=True)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response({'status': True}, status=status.HTTP_200_OK)
            else:
                return Response({'status': False, 'error': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы(Password)'})


class ContactView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        получение контактов
        '''
        contact = Contact.objects.filter(user__id=request.user.id)
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        добавление контакта
        '''
        if {'city', 'street', 'phone'}.issubset(request.data):
            request.data._mutable = True
            request.data.update({'user': request.user.id})
            serializer = ContactSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'status': True}, status=status.HTTP_201_CREATED)
            else:
                Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        '''
        изменение контакта
        '''
        if {'id'}.issubset(request.data):
            try:
                contact = Contact.objects.get(pk=int(request.data["id"]))
            except ValueError:
                return Response(
                    {'status': False, 'error': 'Неверный тип поля ID.'}, status=status.HTTP_400_BAD_REQUEST)

            serializer = ContactSerializer(contact, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': True}, status=status.HTTP_200_OK)
            return Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        '''
        удаление контакта
        '''
        if {'items'}.issubset(request.data):
            for item in request.data["items"].split(','):
                try:
                    contact = Contact.objects.get(pk=int(item))
                    contact.delete()
                except ValueError:
                    return Response({'status': False, 'error': 'Неверный тип поля (items).'},
                                    status=status.HTTP_400_BAD_REQUEST)

            return Response({'status': True}, status=status.HTTP_204_NO_CONTENT)

        return Response({'status': False, 'error': 'Не указаны ID контактов'},
                        status=status.HTTP_400_BAD_REQUEST)

class ProviderUpdate(APIView):
    '''
    Обновить или добавить прайс лист магазина (если магазина нет то он создатся)
    '''
    permission_classes = [IsAuthenticated]
    throttle_scope = 'change_price'

    def post(self, request, *args, **kwargs):
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        url = request.data.get('url')
        if url:
            validate_url = URLValidator()
            try:
                validate_url(url)
            except ValidationError as e:
                return Response({'status': False, 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                stream = get(url).content

                data = load_yaml(stream, Loader=Loader)

                shop, _ = Shop.objects.get_or_create(user_id=request.user.id,
                                                     defaults={'name': data['shop'], 'url': url})
                if shop.name != data['shop']:
                    return Response({'status': False, 'error': 'В файле указано некорректное название магазина!'},
                                    status=status.HTTP_400_BAD_REQUEST)

                return Response({'status': True})

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class ProviderState(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        получение статуса магазина
        '''
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        shop = request.user.shop
        serializer = ShopSerializer(shop)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        изменить статус магазина
        '''
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        state = request.data.get('state')
        if state:
            try:
                Shop.objects.filter(user_id=request.user.id).update(state=strtobool(state))
                return Response({'status': True})
            except ValueError as error:
                return Response({'status': False, 'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'status': False, 'error': 'Не указано поле "Статус".'}, status=status.HTTP_400_BAD_REQUEST)


class ProviderOrders(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        получение сформированныз заказов посавщиками
        '''
        if request.user.type != 'shop':
            return Response({'status': False, 'error': 'Только для магазинов'}, status=status.HTTP_403_FORBIDDEN)

        pr = Prefetch('ordered_items', queryset=OrderItem.objects.filter(shop__user_id=request.user.id))
        order = Order.objects.filter(
            ordered_items__shop__user_id=request.user.id).exclude(status='cart')\
            .prefetch_related(pr).select_related('contact').annotate(
            total_sum=Sum('ordered_items__total_amount'),
            total_quantity=Sum('ordered_items__quantity'))

        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)


class ShopView(ListAPIView):
    '''
    просмотр списка магазинов
    '''
    queryset = Shop.objects.filter(state=True)
    serializer_class = ShopSerializer

class CategoryView(ListAPIView):
    '''
    просмотр категорий
    '''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductView(APIView):
    '''
    поиск всех или определеных товаров
    '''
    def get(self, request, *args, **kwargs):

        query = Q(shop__state=True)
        shop_id = request.query_params.get('shop_id')
        category_id = request.query_params.get('category_id')

        if shop_id:
            query = query & Q(shop_id=shop_id)

        if category_id:
            query = query & Q(category_id=category_id)

        queryset = Product.objects.filter(
            query).select_related(
            'shop', 'category').prefetch_related(
            'product_parameters').distinct()

        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        '''
        получить содержимое корзины
        '''
        cart = Order.objects.filter(
            user_id=request.user.id, status='cart').prefetch_related(
            'ordered_items').annotate(
            total_sum=Sum('ordered_items__total_amount'),
            total_quantity=Sum('ordered_items__quantity'))

        serializer = OrderSerializer(cart, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        '''
        добавление товаров в корзину
        '''
        items = request.data.get('items')
        if items:
            try:
                items_dict = load_json(items)
            except ValueError:
                Response({'Status': False, 'Errors': 'Неверный формат запроса'})
            else:
                cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
                objects_created = 0
                for order_item in items_dict:
                    order_item.update({'order': cart.id})
                    product = Product.objects.filter(external_id=order_item['external_id']).values('category', 'shop', 'name', 'price')
                    order_item.update({'category': product[0]['category'], 'shop': product[0]['shop'], 'product_name': product[0]['name'], 'price': product[0]['price']})
                    serializer = OrderItemAddSerializer(data=order_item)
                    if serializer.is_valid():
                        try:
                            serializer.save()
                        except IntegrityError as error:
                            return Response({'status': False, 'errors': str(error)},
                                            status=status.HTTP_400_BAD_REQUEST)
                        else:
                            objects_created += 1
                    else:
                        return Response({'status': False, 'error': serializer.errors},
                                        status=status.HTTP_400_BAD_REQUEST)
                return Response({'status': True, 'num_objects': objects_created})

        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        '''
        изменение кол-ва конкретного товара в корзине
        '''
        items = request.data.get('items')
        if items:
            try:
                items_dict = load_json(items)
            except ValueError:
                Response({'Status': False, 'Errors': 'Неверный формат запроса'})
            else:
                cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
                objects_updated = 0
                for order_item in items_dict:
                    if isinstance(order_item['id'], int) and isinstance(order_item['quantity'], int):
                        objects_updated += OrderItem.objects.filter(order_id=cart.id, id=order_item['id']).update(
                            quantity=order_item['quantity'])

                return Response({'status': True, 'edit_objects': objects_updated})
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        '''
        удаление товара в корзине
        '''
        items = request.data.get('items')
        if items:
            items_list = items.split(',')
            cart, _ = Order.objects.get_or_create(user_id=request.user.id, status='cart')
            query = Q()
            objects_deleted = False
            for order_item_id in items_list:
                if order_item_id.isdigit():
                    query = query | Q(order_id=cart.id, id=order_item_id)
                    objects_deleted = True

            if objects_deleted:
                deleted_count = OrderItem.objects.filter(query).delete()[0]
                return Response({'status': True, 'del_objects': deleted_count}, status=status.HTTP_204_NO_CONTENT)
        return Response({'status': False, 'error': 'Не указаны необходимые поля'},
                        status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        '''
        получение товаров покупателями
        '''
        order = Order.objects.filter(
            user_id=request.user.id).exclude(status='cart').select_related('contact').prefetch_related(
            'ordered_items').annotate(
            total_quantity=Sum('ordered_items__quantity'),
            total_sum=Sum('ordered_items__total_amount')).distinct()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'Status': False, 'Error': 'Log in required'}, status=403)

        if {'id', 'contact'}.issubset(request.data):
            if request.data['id'].isdigit():
                try:
                    is_updated = Order.objects.filter(
                        user_id=request.user.id, id=request.data['id']).update(
                        contact_id=request.data['contact'],
                        status='new')
                except IntegrityError as error:
                    print(error)
                    return Response({'Status': False, 'Errors': 'Неправильно указаны аргументы'})
                else:
                    if is_updated:
                        return Response({'Status': True})

        return Response({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})
