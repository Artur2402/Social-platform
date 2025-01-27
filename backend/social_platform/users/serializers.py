from django.contrib.auth import get_user_model
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()  # Use the custom user model
    # User info to be input during registration
    fields = ('username', 'email', 'password')
    extra_kwargs = {
        # Make password write-only for security
        'password': {'write_only': True},
    }

  def create(self, validated_data):
    user = get_user_model().objects.create_user(**validated_data)
    return user
