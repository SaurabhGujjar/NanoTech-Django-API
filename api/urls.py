from django.urls import path, include
from .views import UserViewSet, IndexViewSet
from rest_framework import routers
router = routers.DefaultRouter()
# router.register('index', IndexViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('index/', IndexViewSet.as_view(), name="index")
]
