from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('admin')
    MEMBER = 'member', _('member')
    MODERATOR = 'moderator', _('moderator')


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', UserRoles.ADMIN)
        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_('Email'))
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)
    first_name = models.CharField(max_length=30, verbose_name=_('First name'), **NULLABLE)
    last_name = models.CharField(max_length=30, verbose_name=_('Last name'), **NULLABLE)
    phone_number = models.CharField(max_length=20, verbose_name=_('Phone number'), **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name=_('Is active'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
        ordering = ['last_name', 'first_name']
