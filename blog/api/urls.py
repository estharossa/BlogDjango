from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('user/', views.UserDetail.as_view()),
    path('users/posts/', views.PostList.as_view(), name='post-list'),
    path('users/posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('register/', views.RegisterView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
