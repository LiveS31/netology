from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
#импорируум по пользователи и анониму
from rest_framework.decorators import action

from .filters import AdvertisementFilter
from .serializers import AdvertisementSerializer, FavoriteSerializer
from .pemissions import IsAdvertisementOwner
from .models import Advertisement, Favorite, AdvertisementStatusChoices

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Advertisement.objects.all() #читать данные
    # из базы данных, фильтровать и изменять их порядок
    serializer_class = AdvertisementSerializer #чтение, создание, обновление, удаление)
    filterset_class = AdvertisementFilter #просматривать код
    # в соответствии с нашими требованиями
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsAdvertisementOwner()]
        elif self.action in ['add_favorite', 'favorite']:
            return [IsAuthenticated()]
        return []


    def get_queryset(self):
        queryset = Advertisement.objects.all()
        if not self.request.user.is_authenticated:
            queryset = queryset.exclude(status=AdvertisementStatusChoices.DRAFT)
        else:
            queryset =queryset.filter(creator=self.request.user) | queryset.exclude(status='OPEN')
        return queryset

    @action(detail=True, methods=['post'])
    def add_favorite(self, request, pk=None):
        advertisement = self.get_object()
        if advertisement.creator == request.user:
            return Response({'Ошибка! невозможно добавить в избранное'})
        favorite = Favorite.objects.create(user=request.user, advertisement=advertisement)
        serializer = FavoriteSerializer(favorite)
        return Response(serializer.data)

    @action(detail=True, method=['get'])
    def favortes(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        advertisements = [favorites.advertisement for favorite in favorites]
        serializer = AdvertisementSerializer(advertisements, many=True)
        return Response(serializer.data)