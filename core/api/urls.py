from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename="users")


urlpatterns = [
    path('/', include(router.urls)),
    path('/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),

    
    path('api-auth/', include('rest_framework.urls')),
]
