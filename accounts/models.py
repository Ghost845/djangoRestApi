from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.hashers import identify_hasher, make_password
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, full_name=None, is_staff=None, is_admin=None, is_active=True):

        if not email:
            raise ValueError('Пользователь должен ввести адрес электронной почты')
        if not password:
            raise ValueError('Пользователь должен ввести пароль')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.is_active = is_active
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, full_name=None):
        user = self.create_user(email, password=password, full_name=full_name,
                                is_staff=True, is_admin=True)
        return user

    def create_staffuser(self, email, password=None, full_name=None):
        user = self.create_user(email, password=password, full_name=full_name,
                                is_staff=True, is_admin=False)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.full_name:
            return self.full_name
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        if self.admin:
            return True
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    def save(self, *args, **kwargs):
        try:
            _alg = identify_hasher(self.password)
        except ValueError:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
