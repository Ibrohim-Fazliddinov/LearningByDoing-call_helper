from users.urls import urlpatterns as user_url
from api.spectacular.urls import urlpatterns as doc_api
from django.urls import path, include
from organithations.urls import urlpatterns as organisations_url
from breaks.urls import urlpatterns as breaks_url

api_name = 'api'

urlpatterns = [
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += doc_api
urlpatterns += user_url
urlpatterns += breaks_url
urlpatterns += organisations_url
