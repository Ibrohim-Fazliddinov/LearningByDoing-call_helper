from django.urls import path
from users.views import RegisterView, ChangePasswordView, AuthView

urlpatterns = [
    path('users/reg', RegisterView.as_view(), name='register'),
    path('users/ch-pass', ChangePasswordView.as_view(), name='ch-password'),
    path('users/auth', AuthView.as_view(), name='profile')
]
