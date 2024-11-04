from django.urls import path, include

api_name='api'

urlpatterns=[
    path('auth/', include('djoser.urls.jwt')),
]

from api.spectacular.urls import urlpatterns as doc_api
urlpatterns += doc_api