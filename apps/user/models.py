from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Permission
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class CustomUserManager(BaseUserManager):
    def create_user(self, email, nome, password=None):
        if not email:
            raise ValueError('Usuarios devem ter emails validos!')

        user = self.model(
            email=self.normalize_email(email),
            nome=nome,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, password):
        user = self.create_user(
            email=email,
            password=password,
            nome=nome,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(u'nome', max_length=100, null=True, blank=True)
    email = models.EmailField(u'email', max_length=255, null=True, unique=True)
    telefone = models.CharField('numero de telefone', max_length=30, null=True, blank=True)
    data_nasc = models.DateField(null=True, blank=True)
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
        return self.nome

    def save(self, *args, **kwargs):
        super(User, self).save()

    @property
    def first_name(self):
        return self.nome.split(' ')[0]