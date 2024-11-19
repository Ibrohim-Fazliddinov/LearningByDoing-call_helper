from django.contrib.auth import get_user_model
from django.db import models

from breaks.models.dicts import ReplacementStatus
from breaks.models.groups import Group
User = get_user_model()




class Replacement(models.Model):
    group = models.ForeignKey(
        to=Group,
        on_delete=models.CASCADE,
        related_name = 'replacements',
        verbose_name='Group'
    )
    data = models.DateField(verbose_name='Дата смены')
    break_start = models.TimeField(verbose_name='Начало обеда')
    break_end = models.TimeField(verbose_name='Конец обеда')
    break_max_duration = models.PositiveSmallIntegerField(
        verbose_name='Макс. продолжительность обеда'
    )

    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        ordering = ('-data',)

    def __str__(self):
        return f'Смена {self.pk} | для  {self.group}'


class ReplacementEmployee(models.Model):
    replacement = models.ForeignKey(
        to=Replacement,
        on_delete=models.CASCADE,
        related_name='employees',
        verbose_name='Смена'
    )
    employee = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='replacements',
        verbose_name='Сотрудник',
    )
    status = models.ForeignKey(
        to=ReplacementStatus,
        on_delete=models.RESTRICT,
        related_name='replacement_employees',
        verbose_name='Статус смены'
    )

    class Meta:
        verbose_name = 'Смена | Работник'
        verbose_name_plural = 'Смены | Работники'
        ordering = ('status',)

    def __str__(self):
        return f'Смена {self.replacement} | для  {self.employee}'