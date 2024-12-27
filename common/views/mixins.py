from drf_spectacular.openapi import AutoSchema
from rest_framework import mixins
# from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet

from common.serializers.mixins import DictMixinSerializer


class ExtendedGenericViewSet(GenericViewSet):
    pass


class ListViewSet(ExtendedGenericViewSet, mixins.ListModelMixin):
    pass

class DictListMixin(ListViewSet):
    serializer_class = DictMixinSerializer
    pagination_class = None
    model = None
# class UpdateViewSet(ExtendedGenericViewSet, mixins.UpdateModelMixin):
#     pass
class LCRUViewSet(ExtendedGenericViewSet,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin, ):
    pass


class LCRUDViewSet(LCRUViewSet,
                   mixins.DestroyModelMixin, ):
    pass


class LCUViewSet(ExtendedGenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin, ):
    pass


class LCDViewSet(ExtendedGenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.DestroyModelMixin, ):
    pass
