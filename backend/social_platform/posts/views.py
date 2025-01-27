from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import PermissionDenied
from django_filters import rest_framework as django_filters
from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .filters import PostFilter


class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  serializer_class = PostSerializer
  filter_backends = (filters.OrderingFilter,
                     django_filters.DjangoFilterBackend)
  filterset_class = PostFilter
  ordering_fields = ['created_at']
  ordering = ['-created_at']
  permission_classes = [IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

  def perform_update(self, serializer):
    if serializer.instance.author != self.request.user:
      raise PermissionDenied("You do not have permission to edit this post.")
    serializer.save()

  def perform_destroy(self, instance):
    if instance.author != self.request.user:
      raise PermissionDenied("You do not have permission to delete this post.")
    instance.delete()


class CommentViewSet(viewsets.ModelViewSet):
  queryset = Comment.objects.all()
  serializer_class = CommentSerializer
  permission_classes = [IsAuthenticatedOrReadOnly]

  def perform_create(self, serializer):
    serializer.save(author=self.request.user)

  def perform_update(self, serializer):
    if serializer.instance.author != self.request.user:
      raise PermissionDenied(
          "You do not have permission to edit this comment.")
    serializer.save()

  def perform_destroy(self, instance):
    if instance.author != self.request.user:
      raise PermissionDenied(
          "You do not have permission to delete this comment.")
    instance.delete()
