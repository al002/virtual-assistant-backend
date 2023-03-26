from django.urls import path
from .views import BashExecutorView
from .views import login_view, ConversationListCreateAPIView, ConversationRetrieveUpdateDestroyAPIView, ChatMessageListAPIView, ChatMessageDestroyAPIView

urlpatterns = [
    path('bash/executor', BashExecutorView.as_view(), name='bash'),
    path('auth/login', login_view, name='login'),
    path('conversations', ConversationListCreateAPIView.as_view(), name='conversation_list_create'),
    path('conversations/<int:pk>', ConversationRetrieveUpdateDestroyAPIView.as_view(), name='conversation_retrieve_update_destroy'),
    path('conversations/<int:conversation_id>/messages', ChatMessageListAPIView.as_view(), name='chat_message_list'),
    path('conversations/<int:conversation_id>/messages/<int:pk>', ChatMessageDestroyAPIView.as_view(), name='chat_message_delete'),
]
