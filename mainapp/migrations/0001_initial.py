# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-27 06:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire_time', models.DateTimeField(auto_created=True, blank=True, editable=False, null=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('country_code', models.CharField(blank=True, default='+1', max_length=5)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email_verified', models.IntegerField(blank=True, default=0, null=True)),
                ('mobile_verified', models.IntegerField(blank=True, default=0, null=True)),
                ('mobile_code', models.IntegerField(blank=True, null=True)),
                ('forgot_code', models.CharField(blank=True, max_length=5, null=True)),
                ('property_remaining_count', models.IntegerField(blank=True, default=0, null=True)),
                ('parent_id', models.IntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('profile_pic', models.TextField(blank=True, default='', null=True)),
                ('logo_pic', models.TextField(blank=True, default='', null=True)),
                ('company_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('city_name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, default='', max_length=15, null=True)),
                ('street_address', models.TextField(blank=True, default='', null=True)),
                ('state_code', models.CharField(blank=True, default='', max_length=5, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='auth.Group')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
            ],
            options={
                'db_table': 'auth_users',
            },
            managers=[
                ('objects', mainapp.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city_name', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=16, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('iso', models.CharField(blank=True, max_length=2, null=True)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('nic_name', models.CharField(blank=True, max_length=150, null=True)),
                ('country_code', models.CharField(blank=True, max_length=3, null=True)),
                ('numcode', models.IntegerField(blank=True, null=True)),
                ('phonecode', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'countries',
            },
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state_code', models.CharField(blank=True, max_length=2, null=True)),
                ('state_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Countries')),
            ],
            options={
                'db_table': 'states',
            },
        ),
        migrations.CreateModel(
            name='Statuses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'statuses',
            },
        ),
        migrations.CreateModel(
            name='UserAdmins',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(default=0)),
                ('is_dashboard', models.BooleanField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_admins',
            },
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_city', to='mainapp.States'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='state',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state', to='mainapp.States'),
        ),
        migrations.AddField(
            model_name='myuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
