from rest_framework.viewsets import ModelViewSet
from times.models import UserProfile, UserPunch
from times.api.serializers import UserProfileSerializer, UserPunchSerializer


class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class UserPunchViewSet(ModelViewSet):
    queryset = UserPunch.objects.all()
    serializer_class = UserPunchSerializer
