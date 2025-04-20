from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext as _

class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    """
    The account management for system
    Admin: access with system over /admin path
    Employee: (HR, ...) access over portal
    """
    email = models.EmailField(_("Email"), unique=True)
    is_superuser = models.BooleanField(_("Is Superuser"), default=False)
    is_staff = models.BooleanField(_("Is Staff"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=True)
    avatar = models.FileField(_("Avatar"), blank=True, default=None)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    objects = AccountManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Employee(models.Model):
    GENDER_CHOICES = (
        ('0', _("Male")),
        ('1', _("Female")),
        ('2', _("Other")),
    )
    id = models.CharField(_("ID"), unique=True, primary_key=True, max_length=10)
    first_name = models.CharField(_("First Name"), max_length=256)
    last_name = models.CharField(_("Last Name"), max_length=256, blank=True, null=True)
    birth_day = models.DateField(_("Date of Birth"), blank=True, null=True)
    gender = models.CharField(_("Gender"), choices=GENDER_CHOICES, max_length=1)
    phone = models.CharField(_("Phone"), max_length=128, blank=True, null=True)
    address = models.TextField(_("Address"), blank=True, null=True)
    hire_date = models.DateField(_("Hire Date"), blank=True)
    termination_date = models.DateField(_("Termination Date"), blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='employees', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.id})"
    
    def fullname(self):
        return f"{self.first_name} {self.last_name}"
    fullname.short_description = _("Full Name")