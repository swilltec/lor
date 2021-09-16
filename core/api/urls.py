from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")
router.register(r'characters', views.LorViewSet, basename="characters")


urlpatterns = [
    path('', include(router.urls)),
    path('', include('dj_rest_auth.urls')),
    path('signup', include('dj_rest_auth.registration.urls')),
]
