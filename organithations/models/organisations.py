from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from common.models.mixins import InfoMixin

User = get_user_model()


class Organisation(InfoMixin):
    name = models.CharField('Организация', max_length=255)
    director = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='organisations_directors',
        verbose_name='Директор'

    )
    employees = models.ManyToManyField(
        to=User,
        related_name='organisations_employees',
        verbose_name='Сотрудники',
        blank=True,
        through='Employee'
    )

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} | {self.pk}'


class Employee(models.Model):
    organisation = models.ForeignKey("Organisation", verbose_name=(
        "org"), related_name='employees_info', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=(
        "user"), related_name='organisations_info', on_delete=models.CASCADE)
    position = models.ForeignKey("Position", verbose_name=(
        "position"), related_name='employees', on_delete=models.RESTRICT)
    date_joined = models.DateField(
        default=timezone.now, verbose_name='Data Joined')

    class Meta:
        verbose_name = 'Сотрудник Организация'
        verbose_name_plural = 'Сотрудники Организации'
        ordering = ('-date_joined',)
        unique_together = ('organisation', 'user')

    def __str__(self):
        return f'Employee {self.user}'
