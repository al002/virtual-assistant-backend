from django.urls import path
from .views import ChatView
from .views import BashExecutorView

urlpatterns = [
    path('chat/', ChatView.as_view(), name='chat'),
    path('bash/executor/', BashExecutorView.as_view(), name='bash')
]
