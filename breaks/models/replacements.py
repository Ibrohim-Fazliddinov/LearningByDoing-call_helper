from django.contrib.auth import get_user_model
from django.db import models
from breaks.models.dicts import ReplacementStatus
from organithations.models.groups import Group
User = get_user_model()


class GroupInfo(models.Model):
    group = models.OneToOneField(
        to=Group,
        on_delete=models.CASCADE,
        related_name='break_info',
        verbose_name='Group',
        primary_key=True
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

    break_max_duration = models.PositiveSmallIntegerField(
        verbose_name='Максимальная длительность обеда',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'Параметры обеденных перерывов'
        verbose_name_plural = 'Параметры обеденных перерывов'

    def __str__(self):
        return f'{self.name} | {self.pk}'


class Replacement(models.Model):
    group = models.ForeignKey(
        to=GroupInfo,
        on_delete=models.CASCADE,
        related_name='replacements',
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
