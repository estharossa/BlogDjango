from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import serializers
from django.contrib.auth.models import User
from .models import Post
from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        print(self.request.__dict__)
        return self.request.user


class PostList(generics.ListCreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = IsAuthenticated,

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.filter(owner_id=self.request.user.id)
