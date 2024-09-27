from django.urls import path, include
from . import views
from .views import CustomLoginView



app_name = "accounts"
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', views.register, name='register'),
    path('confirm-email/', views.confirm_email, name="confirm_email"),
    
    path('api/profiles/', views.ProfileList.as_view(), name='profile-list'),
    path('api/profiles/<int:pk>/', views.ProfileDetail.as_view(), name='profile-detail'),
]