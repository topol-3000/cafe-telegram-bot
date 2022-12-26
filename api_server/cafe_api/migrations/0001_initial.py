# Generated by Django 4.1.4 on 2022-12-25 20:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Specifies when the entity was created.', verbose_name='created at')),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now, help_text='Specifies when the entity was updated.', verbose_name='updated at')),
                ('phone_number', models.CharField(error_messages={'unique': 'A user with that phone number already exists.'}, max_length=12, unique=True)),
                ('first_name', models.CharField(blank=True, help_text="The user's first name", max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, help_text="The user's last name", max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, help_text="The user's last email", max_length=150, verbose_name='email')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'admin user',
                'verbose_name_plural': 'admin users',
            },
        ),
    ]
