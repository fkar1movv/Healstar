from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, get_object_or_404
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from chat.models import Chat, ChatHistory
from chat.serializers import ChatHistorySerializer
from chat.filters import ChatHistoryFilterSet


class CreateChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        new_chat = Chat.objects.create(**request.data)

        return Response({'chat_id': new_chat.id}, status=201)


class RetrieveChatAPIView(APIView):

    def get(self, request, *args, **kwargs):
        chat = Chat.objects.filter(**kwargs)

        if chat.exists():
            return Response({'chat_exists': True}, status=200)

        return Response({'chat_exists': False}, status=404)


class CreateChatHistoryAPIView(CreateAPIView):
    serializer_class = ChatHistorySerializer


class RetrieveChatHistoryAPIView(GenericAPIView):
    serializer_class = ChatHistorySerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ChatHistoryFilterSet

    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True).data

        return Response(serializer)

    def get_object(self):
        chat = get_object_or_404(Chat, **self.kwargs)

        return chat

    def get_queryset(self):
        chat = self.get_object()

        queryset = ChatHistory.objects.filter(chat_id=chat.id)

        return queryset
