from django_filters import rest_framework as django_filters
from .models import Post


class PostFilter(django_filters.FilterSet):
  category = django_filters.CharFilter(lookup_expr='icontains')
  author = django_filters.CharFilter(field_name='author__id')
  created_at = django_filters.DateFromToRangeFilter()

  class Meta:
    model = Post
    fields = ['category', 'author', 'created_at']
