import django_filters
from .models import UserFile

class UserFileFilter(django_filters.FilterSet):
    ext = django_filters.CharFilter(method='filter_by_extension')
    uploaded_from = django_filters.DateFilter(field_name='uploaded_at', lookup_expr='gte')
    uploaded_to = django_filters.DateFilter(field_name='uploaded_at', lookup_expr='lte')

    class Meta:
        model = UserFile
        fields = ['file_type']

    def filter_by_extension(self, queryset, name, value):
        return queryset.filter(original_filename__iendswith=f".{value.lower()}")
