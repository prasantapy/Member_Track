from django.contrib import admin
from django.urls import path,include
from api import views as v
from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register('api',v.member_view)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',v.member_view.as_view({'get': 'list'})),
    #path('',include(routers.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh token
]


