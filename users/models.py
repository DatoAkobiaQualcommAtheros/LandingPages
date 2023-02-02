from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            msg = "Users must have an email"
            raise ValueError(msg)

        ft_user = self.model(
            email=UserManager.normalize_email(email),
        )

        ft_user.set_password(password)
        ft_user.save(using=self._db)
        return ft_user

    def create_superuser(self, email, password=None):
        ft_user = self.create_user(
            email,
            password=password,
        )

        ft_user.is_admin = True
        ft_user.is_staff = True
        ft_user.is_superuser = True
        ft_user.save(using=self._db)
        return ft_user

    def get_by_natural_key(self, email):
        return self.get(**{User.USERNAME_FIELD+"__iexact": email})

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(verbose_name='email address', max_length=254, unique=True, db_index=True)
    phone = models.CharField(default=None, max_length=50, null=True, blank=True)

    USERNAME_FIELD = 'email'

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email


