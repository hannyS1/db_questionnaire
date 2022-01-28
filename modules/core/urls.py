from django.urls import path, include
from rest_framework.routers import DefaultRouter

from modules.core.api import AuthorizationApi

router = DefaultRouter()
router.register('auth', AuthorizationApi, basename='auth')


urlpatterns = [
    path('', include(router.urls)),
]
