from django.urls import path, include
from rest_framework.routers import DefaultRouter

from breaks.views import dicts

router = DefaultRouter()

router.register(r'dicts/stasuses/breaks', dicts.BreakStatusView, 'breaks')
router.register(r'dicts/stasuses/replacements', dicts.ReplacementStatusView, 'replacement')

urlpatterns = [
    path('breaks/', include(router.urls)),
]
