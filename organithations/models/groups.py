from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from organithations.models.organisations import Organisation
from common.models.mixins import InfoMixin

User = get_user_model()


class Group(InfoMixin):
    organisation = models.ForeignKey(
        to=Organisation,
        on_delete=models.CASCADE,
        related_name='groups',
        verbose_name='Организация',
    )
    name = models.CharField(verbose_name='Название', max_length=255)
    manager = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='groups_managers',
        verbose_name='Менеджер',
    )
    members = models.ManyToManyField(
        to=User,
        related_name='groups_members',
        verbose_name='Сотрудники',
        blank=True,
        through='Member'
    )

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} | {self.pk}'


class Member(models.Model):
    group = models.ForeignKey("Group", verbose_name=(
        "org"), related_name='members_info', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=(
        "user"), related_name='group_info', on_delete=models.CASCADE)

    date_joined = models.DateField(
        default=timezone.now, verbose_name='Data Joined')

    class Meta:
        verbose_name = 'Участник группы'
        verbose_name_plural = 'участники группы'
        ordering = ('-date_joined',)
        unique_together = ('group', 'user')

    def __str__(self):
        return f'Group {self.user}'
