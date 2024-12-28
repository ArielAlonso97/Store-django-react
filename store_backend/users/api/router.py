from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .viewSets import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto incluye todas las URLs del router
]