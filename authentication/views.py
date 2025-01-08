import re
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import UserProfile
from .serializers import UserProfileSerializer
from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate

class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['role'] = user.userprofile.role
        return token

    def validate(self, attrs):
        username_or_email = attrs.get('username')
        password = attrs.get('password')

        # Normalize the input (for case-insensitive matching)
        normalized_input = username_or_email.lower()

        # Check if the input is an email or username
        if '@' in normalized_input:
            try:
                user = User.objects.get(email__iexact=normalized_input)  # Case-insensitive email lookup
                attrs['username'] = user.username  # Normalize the username for consistency
            except User.DoesNotExist:
                raise serializers.ValidationError({"detail": "Email not found."})
        else:
            try:
                user = User.objects.get(username__iexact=normalized_input)  # Case-insensitive username lookup
                attrs['username'] = user.username  # Normalize the username for consistency
            except User.DoesNotExist:
                raise serializers.ValidationError({"detail": "Username not found."})

        user = authenticate(username=attrs['username'], password=password)

        # Case 1: If authentication fails (incorrect password)
        if user is None:
            raise serializers.ValidationError({"detail": "Invalid password."})

        # Ensure the user has a profile with a role assigned
        try:
            user_profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError({"detail": "User role not assigned."})

        # Role-based login validation
        requested_role = self.context['request'].data.get('role', None)
        if requested_role and user_profile.role != requested_role:
            raise serializers.ValidationError({
                "detail": f"Invalid role. This account is associated with the '{user_profile.role.capitalize()}' role."
            })

        # Add username and role to the response data
        data = super().validate(attrs)
        data['username'] = user.username
        data['role'] = user_profile.role

        return data

class LoginTokenObtainPairView(TokenObtainPairView):
    serializer_class = LoginTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def registerUser(request):
    """
    Register a new user with a role and return a token.
    """
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    role = request.data.get('role')  # 'admin', 'teacher', or 'student'

    # Check for required fields
    if not username or not email or not password or not role:
        return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

    # Validate username: only letters, numbers, and underscores allowed, can't start with a number
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', username):
        return Response({
            "error": "Username can only contain letters, numbers, and underscores, and cannot start with a number and underscore."
        }, status=status.HTTP_400_BAD_REQUEST)

    # Disallow '@' in username
    if '@' in username:
        return Response({"error": "Username cannot contain '@'."}, status=status.HTTP_400_BAD_REQUEST)

    # Check that the username is not purely numeric
    if username.isdigit():
        return Response({"error": "Username cannot be only numbers."}, status=status.HTTP_400_BAD_REQUEST)

    # Ensure username is at least 4 characters long
    if len(username) < 4:
        return Response({"error": "Username must be at least 4 characters long."}, status=status.HTTP_400_BAD_REQUEST)

    if role not in ['admin', 'teacher', 'student']:
        return Response({"error": "Invalid role. Valid roles are: admin, teacher, student."}, status=status.HTTP_400_BAD_REQUEST)

    # Normalize email and username to lowercase for consistency
    email = email.lower()
    username = username.lower()

    # Case-insensitive checks for username and email
    if User.objects.filter(username__iexact=username).exists():
        return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(email__iexact=email).exists():
        return Response({"error": "Email already exists."}, status=status.HTTP_400_BAD_REQUEST)

    # Validate email format
    try:
        EmailValidator()(email)
    except ValidationError:
        return Response({"error": "Invalid email format."}, status=status.HTTP_400_BAD_REQUEST)

    # Validate password strength
    try:
        validate_password(password)
    except ValidationError as e:
        error_messages = [str(msg) for msg in e.messages]
        return Response({"error": error_messages}, status=status.HTTP_400_BAD_REQUEST)

    # Create user and profile
    user = User.objects.create_user(username=username, email=email, password=password)
    user_profile = UserProfile.objects.create(user=user, role=role)

    # Generate token for the new user
    refresh = RefreshToken.for_user(user)
    return Response({
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "username": username,
        "role": role
    }, status=status.HTTP_201_CREATED)

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

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'POST': '/register/'},
        {'POST': '/login/'},
        {'POST': '/login/refresh/'},
        {'GET': '/user/profile/'},
        {'POST': '/user/status-update/'},
        {'GET': '/user/check-online/'},
    ]
    return Response(routes)
