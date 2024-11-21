from django.urls import path
from users.views import RegisterView, ChangePasswordView

urlpatterns = [
    path('users/reg', RegisterView.as_view(), name='register'),
    path('users/ch-pass', ChangePasswordView.as_view(), name='change-password')
]

