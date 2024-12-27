from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer
from organithations.models.dicts import Position


User = get_user_model()


class PositionListSerializer(ExtendedModelSerializer):

    class Meta:
        model = Position
        fields = (
            'code',
            'name',
        )

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
