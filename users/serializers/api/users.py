from xml.etree.ElementTree import ParseError
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.db import transaction
from users.serializers.nested.profile import (
    ProfileShortSerializer,
    ProfileUpdateSerializer
)

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name')

    def validate_email(self, value):
        email = value.lower()
        if User.objects.filter(email=email).exists():
            raise ParseError('Email already registered')
        return email

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['old_password', 'new_password']

    def validate(self, attrs):
        user = self.instance
        old_password = attrs.pop('old_password')
        if not user.check_password(old_password):
            raise ParseError('Проверьте правильность паролей')
        return attrs

    def validate_new_password(self, value):
        validate_password(value)
        return value

    def update(self, instance, validated_data):
        password = validated_data.pop('new_password')
        instance.set_password(password)
        instance.save()
        return instance


class AuthSerializer(serializers.ModelSerializer):
    profile = ProfileShortSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'profile'
        )


class AuthUpdateSerializer(serializers.ModelSerializer):
    profile = ProfileUpdateSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'profile'
        )

    def update(self, instance, validated_data):
        # Проверка наличия профиля
        profile_data = validated_data.pop(
            'profile') if 'profile' in validated_data else None
        with transaction.atomic():
            instance = super().update(instance, validated_data)
        self._update_profile(instance.profile, profile_data)
        return instance

    def _update_profile(self, profile, profile_data):
        profile_serializer = ProfileUpdateSerializer(
            instance=profile, data=profile_data, partial=True
        )
        profile_serializer.is_valid(raise_exception=True)
        profile_serializer.save()
