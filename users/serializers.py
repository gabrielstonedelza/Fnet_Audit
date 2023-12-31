from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from .models import User, Profile


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'phone', 'company_name', 'full_name', 'user_type')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'profile_pic', 'get_profile_pic', 'get_company_name', 'get_phone',
                  'get_email', 'get_username', 'get_usertype']
        read_only_fields = ['user']
