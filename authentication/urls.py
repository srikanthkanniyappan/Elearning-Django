from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('routes/', views.getRoutes),
    path('register/', views.registerUser, name='register_user'),
    path('login/', views.LoginTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/profile/', views.getUserProfile, name='user_profile'),
    path('user/status-update/', views.updateUserStatus, name='update_user_status'),
    path('user/check-online/', views.checkUserOnlineStatus, name='check_user_online_status'),
]
