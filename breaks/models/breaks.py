
from django.db import models
from django.contrib.auth import get_user_model

from breaks.const import BREAK_CREATED_STATUS, BREAK_CREATED_DEFAULT
from breaks.models.dicts import BreakStatus
from breaks.models.replacements import Replacement

User = get_user_model()

class Break(models.Model):
    replacement = models.ForeignKey(
        to=Replacement,
        on_delete=models.CASCADE,
        related_name='breaks',
        verbose_name='Смена',
    )
    employee = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='breaks',
        verbose_name='Сотрудник',
    )
    min_active = models.PositiveSmallIntegerField(
        verbose_name='Минимальное кол-во активных сотрудников',
        null=True, blank=True,
    )
    break_start = models.TimeField(
        verbose_name='Начало обеда',
        null=True, blank=True
    )
    break_end = models.TimeField(
        verbose_name='Конец обеда',
        null=True, blank=True
    )
    duration = models.PositiveSmallIntegerField(
        verbose_name='Продолжительность обеда',
        null=True, blank=True
    )

    status = models.ForeignKey(
        to=BreakStatus,
        on_delete=models.RESTRICT,
        related_name='breaks',
        null=False,
        blank=True,
        verbose_name='Статус',
    )

    class Meta:
        verbose_name = 'Обеденный перерыв'
        verbose_name_plural = 'Обеденный перерывы'
        ordering = ('-replacement__data','break_start')

    def __str__(self):
        return f'Обед пользователя {self.employee} | {self.pk}'


    def save(self, *args, **kwargs):
        if not self.pk:
            status, created = BreakStatus.objects.get_or_create(
                code=BREAK_CREATED_STATUS,
                defaults=BREAK_CREATED_DEFAULT
            )
            self.status = status
        return super(Break, self).save(*args, **kwargs)