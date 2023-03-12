from django.db import models
from devopshobbies.common.models import BaseModel

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager as BUM
from django.contrib.auth.models import PermissionsMixin

from django.core.exceptions import ValidationError

class BaseUserManager(BUM):
    def create_user(self, 
        email, 
        is_active=True,
        is_admin=False, 
        password=None , 
        ID=None , 
        first_name=None , 
        last_name = None):

        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(email=self.normalize_email(email.lower()),
            is_active=is_active, 
            is_admin=is_admin,
            ID = ID , 
            first_name = first_name , 
            last_name=last_name)

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.full_clean()
        user.save(using=self._db)

        return user

    def create_superuser(self, email , ID=None , first_name = None ,  last_name=None ,password=None):
        user = self.create_user(
            email=email,
            is_active=True,
            is_admin=True,
            first_name=first_name,
            last_name=last_name,
            password=password,
            ID = ID
        )

        user.is_superuser = True
        user.save(using=self._db)

        return user




class BaseUser(BaseModel, AbstractBaseUser, PermissionsMixin):

    ID = models.CharField(unique=True , max_length=10 )

    email = models.EmailField(verbose_name = "email address",
                              unique=True)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = BaseUserManager()

    USERNAME_FIELD = "ID"

    def __str__(self):
        return self.email

    def is_staff(self):
        return self.is_admin


class Profile(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE)
    posts_count = models.PositiveIntegerField(default=0)
    subscriber_count = models.PositiveIntegerField(default=0)
    subscription_count = models.PositiveIntegerField(default=0)
    bio = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return f"{self.user} >> {self.bio}"






