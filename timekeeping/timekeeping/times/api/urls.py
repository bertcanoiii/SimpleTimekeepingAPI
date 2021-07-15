from django.urls import include, path
from rest_framework.routers import DefaultRouter
from times.api.views import UserProfileViewSet, UserPunchViewSet


router = DefaultRouter()
router.register(r"userprofiles/", UserProfileViewSet)
router.register(r"userpunches/", UserPunchViewSet)

urlpatterns = [
    path("", include(router.urls))
]
