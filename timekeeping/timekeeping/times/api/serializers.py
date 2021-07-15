from rest_framework import serializers
from times.models import UserProfile, UserPunch
from timezone_field.rest_framework import TimeZoneSerializerField


class UserProfileSerializer(serializers.ModelSerializer):

    time_zone = TimeZoneSerializerField()

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserPunchSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPunch
        fields = "__all__"
