from django.urls import path, include
from . import views
from rest_framework import urls, routers
from rest_framework_simplejwt.views import TokenRefreshView


#유저리스트 (테스트용)
router = routers.DefaultRouter()
router.register('list', views.UserViewSet) 

urlpatterns =[
    path('join/', views.RegisterAPIView.as_view()), #회원가입
    path('auth/', views.AuthAPIView.as_view()), #로그인
    path("auth/refresh/", TokenRefreshView.as_view()), #토큰 재발급
    path('', include(router.urls)),
]