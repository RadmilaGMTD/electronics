from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from network.permissions import IsActiveUser

from .models import User
from .serializers import UserSerializer


class UserCreateApiView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserListApiView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsActiveUser]
