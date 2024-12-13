
from common.models.mixins import BaseDictModelMixin


class Position(BaseDictModelMixin):

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        ordering = ('sort',)
