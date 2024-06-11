from django.urls import path

from chat import views

urlpatterns = [
    path('create/', views.CreateChatAPIView.as_view(), name='create-chat'),
    path('detail/<int:doctor_id>/<int:patient_id>/', views.RetrieveChatAPIView.as_view(), name='chat-detail'),
    path('history/create/', views.CreateChatHistoryAPIView.as_view(), name='create-chat-history'),
    path('history/<int:pk>/list/', views.RetrieveChatHistoryAPIView.as_view(), name='list-chat-history')  # pk aka chat_id
]