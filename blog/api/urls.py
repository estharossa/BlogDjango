from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('user/', views.UserDetail.as_view()),
    path('users/posts/', views.PostList.as_view(), name='post-list'),
    path('users/posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('users/posts/<int:pk>/create_comment/', views.CommentCreateView.as_view(), name='create-comment'),
    path('users/posts/<int:pk>/comments/', views.PostCommentsList.as_view(), name='post_comments'),
    path('users/posts/<int:pk>/like/', views.PostLikeToggle.as_view(), name='post_like_toggle'),
    path('register/', views.RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
