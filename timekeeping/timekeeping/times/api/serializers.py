from rest_framework import serializers
from times.models import UserProfile, UserPunch


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = "__all__"


class UserPunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPunch
        fields = "__all__"
