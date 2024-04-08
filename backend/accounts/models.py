from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, fathers_name, birth_date, home_address, phone_number, photo, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            fathers_name=fathers_name,
            birth_date=birth_date,
            home_address=home_address,
            phone_number=phone_number,
            photo=photo,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, fathers_name, birth_date, home_address, phone_number, photo, password):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            fathers_name=fathers_name,
            birth_date=birth_date,
            home_address=home_address,
            phone_number=phone_number,
            photo=photo,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    fathers_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    home_address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    auth_token = models.CharField(max_length=100, blank=True)
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fathers_name', 'birth_date', 'home_address', 'phone_number', 'photo']

    def __str__(self):
        return self.email