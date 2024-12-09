from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST': '/login/'},  # Login endpoint
        {'POST': '/login/refresh/'},  # Refresh login session
        {'GET': '/user/profile/'},  # Get user profile
        {'POST': '/user/status-update/'},  # Get user status
        {'GET': '/user/check-online/'},  # Check if user is online
    ]
    return Response(routes)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    serializer = UserProfileSerializer(user_profile)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def updateUserStatus(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        is_online = request.data.get('is_online')

        # Update user online status
        user_profile.is_online = is_online
        user_profile.save()

        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except UserProfile.DoesNotExist:
        return Response({"error": "UserProfile not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def checkUserOnlineStatus(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return Response({"is_online": user_profile.is_online}, status=status.HTTP_200_OK)
