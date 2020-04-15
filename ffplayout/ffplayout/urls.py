"""ffplayout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from rest_framework import routers
from api import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'guisettings', views.GuiSettingsViewSet, 'guisettings')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/config/', views.Config.as_view()),
    path('api/playlist/', views.Playlist.as_view()),
    path('api/stats/', views.Statistics.as_view()),
    path('api/current/user/', views.CurrentUserView.as_view()),
    path('api/media/', views.Media.as_view()),
    path('api-auth/', include(
         'rest_framework.urls', namespace='rest_framework')),
    path('auth/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    re_path(r'^upload/(?P<filename>[^/]+)$',  views.FileUpload.as_view())
]
