from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import RegisterView, TestProtectedView, MyTokenObtainPairView, ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', MyTokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test/', TestProtectedView.as_view(), name='test-protected'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
