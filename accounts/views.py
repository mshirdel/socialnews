from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User
from . import serializers as auth_serializer


class UserList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = auth_serializer.UserSerializer
    queryset = User.objects.all()


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = auth_serializer.RegisterSerializer

    def post(self, request):
        serialized_data = self.serializer_class(data=request.data)
        serialized_data.is_valid(raise_exception=True)
        serialized_data.save()
        return Response(serialized_data.data, status=status.HTTP_201_CREATED)


class LoginUser(APIView):
    permission_classes = [AllowAny]
    serializer_class = auth_serializer.LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUser(generics.RetrieveUpdateAPIView):
    """
    Retrieve current user info with updateing its data
    """

    permission_classes = [IsAuthenticated]
    serializer_class = auth_serializer.UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request):
        serializer = self.serializer_class(request.user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserInfo(generics.RetrieveAPIView):
    """
    Show general info of users
    """

    permission_classes = [AllowAny]
    serializer_class = auth_serializer.UserSerializer

    def get_queryset(self):
        return User.objects.filter(is_active=True)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
