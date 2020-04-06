# user serializer
from .models import Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # profile=ProfileSerializer()
    class Meta:
        model = User
        fields = [
            'id',
            'url',
            'username',
            'first_name',
            'last_name', 
            'email', 
            # 'profile'
            ]

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = [
            'id',
            'url',
            'user',
            'is_addicted', 
            'current_ammount', 
            'profile_image',
            'joined',
            ]