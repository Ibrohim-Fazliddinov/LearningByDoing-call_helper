from common.views.mixins import DictListMixin
from organithations.models.dicts import Position
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(summary='Список должностей', tags=['Словари']),
)
class PositionView(DictListMixin):
    model = Position

