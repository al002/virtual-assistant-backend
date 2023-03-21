# api/views/login.py
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def login_view(request):
    form = AuthenticationForm(request, data=request.data)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return Response({'detail': '登录成功'}, status=status.HTTP_200_OK)
    return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
