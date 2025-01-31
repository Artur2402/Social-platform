from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from users.serializers import CustomUserSerializer


class RegisterView(APIView):
  def post(self, request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
      user = serializer.save()
      # Create JWT token for the new user
      refresh = RefreshToken.for_user(user)
      return Response({
          'refresh': str(refresh),
          # Return both refresh and access tokens
          'access': str(refresh.access_token),
      }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
