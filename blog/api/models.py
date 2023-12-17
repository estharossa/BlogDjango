from django.db import models


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)
    # likes_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['created']


# todo: bind comments to posts
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', related_name='author', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['created_at']


# class Like(models.Model):
#     user = models.ForeignKey('auth.User', related_name='author', on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
#     liked = models.BooleanField(default=True)  # True for like, False for unlike
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         unique_together = ('user', 'post')
