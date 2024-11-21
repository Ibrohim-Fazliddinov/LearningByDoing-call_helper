from django.urls import path, include

api_name='api'

urlpatterns=[
    path('auth/', include('djoser.urls.jwt')),
]

from api.spectacular.urls import urlpatterns as doc_api
from users.urls import urlpatterns as user_api
urlpatterns += doc_api
urlpatterns += user_api