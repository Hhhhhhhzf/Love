from django.db import models

# Create your models here.
import django.utils.timezone as timezone
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, username, nickname, new_message, is_valid, icon, last_login, create_time, update_time,
                    ip_address, email, upload_address, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            nickname=nickname,
            new_message=new_message,
            is_valid=is_valid,
            icon=icon,
            last_login=last_login,
            create_time=create_time,
            update_time=update_time,
            ip_address=ip_address,
            email=email,
            upload_address=upload_address,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, nickname, new_message, is_valid, icon, last_login, create_time, update_time,
                         ip_address, email, upload_address, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            username,
            nickname,
            new_message,
            is_valid,
            icon,
            last_login,
            create_time,
            update_time,
            ip_address,
            email,
            upload_address,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    nickname = models.CharField(max_length=100)
    new_message = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=True)
    icon = models.ImageField(default="None")
    last_login = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(default="None")
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    upload_address = models.CharField(max_length=300, default="None")
    can_upload = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
