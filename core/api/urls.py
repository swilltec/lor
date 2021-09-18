from django.urls import path, include
from rest_framework.routers import DefaultRouter


from . import views


# Create a router to group views
router = DefaultRouter()
router.register(r"characters", views.LorViewSet, basename="characters")
router.register(r"favorites", views.FavoriteViewSet, basename="favorites")


urlpatterns = [
    path("", include(router.urls)),
    path("", include("dj_rest_auth.urls")),
    path("signup", include("dj_rest_auth.registration.urls")),
]
