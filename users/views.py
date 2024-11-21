from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from users.serializers.api.users import RegisterSerializer, ChangePasswordSerializer

User = get_user_model()


@extend_schema_view(
    post=extend_schema(summary='Регистрация и Аутентификация', tags=['Аутентификация & Авторизация'])
)
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@extend_schema_view(
    post=extend_schema(
        request=ChangePasswordSerializer,
        summary='Смена пароля', tags=['Аутентификация & Авторизация']),
)
class ChangePasswordView(APIView):

    def post(self, request):
        user = request.user
        serializer = ChangePasswordSerializer(
            instance=user, data=request.data
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=HTTP_204_NO_CONTENT)
