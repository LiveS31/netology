from django_filters import rest_framework as filters, DateFromToRangeFilter

from .models import Advertisement



class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    # по дате
    created_at = DateFromToRangeFilter()

    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        #поля для админки
        fields = ['created_at', 'creator', 'status']
