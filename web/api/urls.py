from django.urls import path
from .views import ChatView
from .views import BashExecutorView
from .views import login_view

urlpatterns = [
    path('chat', ChatView.as_view(), name='chat'),
    path('bash/executor', BashExecutorView.as_view(), name='bash'),
    path('auth/login', login_view, name='login')
]
