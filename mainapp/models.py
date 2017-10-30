from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group
import binascii
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from django.conf import settings
from django.contrib.auth import get_user_model

class MyUserManager(UserManager):
    use_in_migrations = True

    def _create_user(self, mobile_no, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        mobile_no = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, mobile_no, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(mobile_no, email, password, **extra_fields)

    def create_superuser(self, mobile_no, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user( mobile_no, email, password, **extra_fields)


class Countries(models.Model):
    id = models.AutoField(primary_key=True)
    iso = models.CharField(max_length=2, blank=True, null=True)
    country_name = models.CharField(max_length=255, blank=True, null=True)
    nic_name = models.CharField(max_length=150, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    numcode = models.IntegerField(blank=True, null=True)
    phonecode = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,null=True, blank=True)

    class Meta:
        db_table = "countries"


class States(models.Model):
    id = models.AutoField(primary_key=True)
    country = models.ForeignKey(Countries)
    state_code = models.CharField(max_length=2, blank=True, null=True)
    state_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = "states"

class MyUser(AbstractUser):
    """@Create auth_users tables"""
    country_code = models.CharField(max_length=5, blank=True,default='+1')
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    mobile_no = models.CharField(max_length=255, blank=True, null=True, unique= True)
    email_verified = models.IntegerField(blank=True, null=True, default=0)
    mobile_verified = models.IntegerField(blank=True, null=True, default=0)
    mobile_code = models.IntegerField (blank=True, null=True)
    forgot_code = models.CharField (max_length=5,blank=True, null=True)
    expire_time = models.DateTimeField (null=True, blank=True,auto_created=True,editable=False)
    property_remaining_count = models.IntegerField(blank=True, null=True,default=0)
    parent_id = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=500,blank=True, null=True, unique=False)
    email = models.EmailField(max_length=255, unique=True)
    profile_pic = models.TextField(blank=True, null=True, default='')
    logo_pic = models.TextField (blank=True, null=True, default='')
    company_name = models.CharField(max_length=255, blank=True, null=True, default='')
    city_name = models.CharField(max_length=255, blank=True, null=True, default='')
    zipcode = models.CharField(max_length=15, blank=True, null=True,default='')
    street_address = models.TextField(blank=True, null=True, default='')
    state = models.ForeignKey(States, related_name='state', blank=True, null=True, default=1)
    state_code = models.CharField (max_length=5, blank=True, null=True, default='')
    group = models.ForeignKey(Group, blank=True, null=True, related_name='role')
    modified = models.DateTimeField(null=True, blank=True, auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobile_no']

    objects = MyUserManager()

    class Meta:
        db_table = "auth_users"


class UserAdmins(models.Model):
    """@Create class for user admins
    admin this is parent id
    user this is user
    """
    id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,related_name='admin')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,related_name='user_info')
    is_deleted = models.BooleanField(blank=True, default=0)
    is_dashboard = models.BooleanField(blank=True, default=0)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = "user_admins"


class Cities(models.Model):
    """@Create class for cities"""
    id = models.AutoField(primary_key=True)
    state = models.ForeignKey(States,related_name='state_city', blank=True,null=True)
    city_name = models.CharField(blank=True, null=True, max_length=255)
    zipcode = models.CharField(blank=True, null=True, max_length=16)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = "cities"


class Statuses(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    modified = models.DateTimeField(auto_now=True,blank=True, null=True)

    class Meta:
        db_table = "statuses"

