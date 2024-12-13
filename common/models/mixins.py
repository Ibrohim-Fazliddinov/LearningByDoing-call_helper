from django.db import models


class BaseDictModelMixin(models.Model):
    code = models.CharField(
        verbose_name='Код',
        max_length=20,
        primary_key=True
    )
    name = models.CharField(verbose_name='Название', max_length=32)
    sort = models.PositiveSmallIntegerField(verbose_name='Сортировка',
                                            null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Активность', default=True)

    class Meta:
        ordering = ('sort',)
        abstract = True

    def __str__(self):
        return f'{self.code} | для  {self.name}'
