from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField  # Correct import for model fields
from users.managers import CustomUserManager
from users.models.profile import Profile


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Никнейм',
        unique=True,
        null=True,
        blank=True,
        max_length=35
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
        null=True,
        blank=True
    )
    phone_number = PhoneNumberField(
        'Телефон',
        unique=True,
        null=True
    )
    objects = CustomUserManager()
    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def full_name(self):
        return f'{self.first_name}|{self.last_name}'

    def __str__(self):
        return f'{self.full_name}'

@receiver(post_save, sender=User)
def post_save(sender, instance, created, **kwargs):
    if not hasattr(instance, 'profile'):
        Profile.objects.create(user=instance)

