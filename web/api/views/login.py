from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'success': True}, status=status.HTTP_200_OK)
    else:
        return Response({'success': False, 'message': 'Invalid email or password'}, status=status.HTTP_400_BAD_REQUEST)
