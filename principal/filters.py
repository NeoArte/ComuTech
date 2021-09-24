import django_filters
from .models import Cliente


class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = '__all__'

        exclude = ['ending_date', 'contributors']