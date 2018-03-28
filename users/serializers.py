from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'password')
    #    extra_kwargs = {'password': {'write_only': True}}
        #extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user


        # def create(self, validated_data):
        #     user = User(
        #         email=validated_data['email'],
        #         username=validated_data['username'],
        #         password=make_password(validated_data['password'])
        #     )
        #     user.save()
        #     return user
