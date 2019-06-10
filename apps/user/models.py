from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, displayName, password=None):
        if not email:
            raise ValueError('Usuarios devem ter emails validos!')

        user = self.model(
            email=self.normalize_email(email),
            displayName=displayName,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, displayName, password):
        user = self.create_user(
            email=email,
            password=password,
            displayName=displayName,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    uid = models.CharField(u'UID', max_length=255, null=True, blank=True)
    photoURL = models.CharField(u'Url foto de perfil', max_length=255, null=True, blank=True)
    providerID = models.CharField(u'provider', max_length=255, null=True, blank=True)
    displayName = models.CharField(u'nome', max_length=100, null=True, blank=True)
    email = models.EmailField(u'email', max_length=255, null=True, unique=True)
    phoneNumber = models.CharField('numero de telefone', max_length=30, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.displayName

    def save(self, *args, **kwargs):
        super(User, self).save()

    @property
    def first_name(self):
        return self.displayName.split(' ')[0]