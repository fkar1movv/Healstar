from django_filters import rest_framework as filters

from chat.models import ChatHistory


class ChatHistoryFilterSet(filters.FilterSet):
    created_gte = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_lte = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = ChatHistory
        fields = (
            'created_gte',
            'created_lte',
            'sender',
        )
