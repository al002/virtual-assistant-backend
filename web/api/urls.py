from django.urls import path
from .views import ChatView
from .views import BashExecutorView
from .views import login_view, ConversationListCreateAPIView, ConversationRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('chat', ChatView.as_view(), name='chat'),
    path('bash/executor', BashExecutorView.as_view(), name='bash'),
    path('auth/login', login_view, name='login'),
    path('conversations', ConversationListCreateAPIView.as_view(), name='conversation-list-create'),
    path('conversations/<int:pk>', ConversationRetrieveUpdateDestroyAPIView.as_view(), name='conversation-retrieve-update-destroy'),
]
