# Create your models here.
import random
import this
import regex as regex
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.core.validators import RegexValidator
from django.db import models



class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email                       = self.normalize_email(email)
        user                        = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):
    username                    = None
    email                       = models.EmailField(max_length=100, unique=True)
    first_name                  = models.CharField(max_length=100)
    last_name                   = models.CharField(max_length=100)
    phone                       = models.CharField(max_length=14) 
    referal_code                = models.CharField(max_length=50,blank=True,null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    # def save(self,*args, **kwargs):
    #     referal_code = self.cleaned_data.get("referal_code")
    #     if referal_code == "":
    #         referal_code ='Torque.in'+str(random.randint(1111111, 9999999))
    #         self.referal_code = referal_code
    #         refer = self.referal_code
    #         return refer
    #     super().save(refer, **kwargs)

        


    


class Profile(models.Model):
    user = models.OneToOneField(Account,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name






