from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from . import serializers
from django.contrib.auth.models import User
from .models import Post, Comment, Like
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
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


class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        post_id = self.kwargs.get('pk')
        serializer.save(post_id=post_id)


class PostCommentsList(generics.ListAPIView):
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('pk')
        return Comment.objects.filter(post_id=post_id)


class PostLikeToggle(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        liked = Like.objects.filter(post=post, user=user).exists()

        if liked:
            Like.objects.filter(post=post, user=user).delete()
            post.likes_count -= 1
            post.save()
            return Response({'liked': False, 'likes_count': post.likes_count}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(post=post, user=user)
            post.likes_count += 1
            post.save()
            return Response({'liked': True, 'likes_count': post.likes_count}, status=status.HTTP_200_OK)
