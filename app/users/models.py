from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from app import crypto

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        """
        Create and save a User with the given email and password
        """
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and save a superuser with the given email and password
        """
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    USERNAME_FIELD ="email"

    is_active = models.BooleanField(default=False, help_text="Designates whether or not the user's account is active")
    is_staff = models.BooleanField(default=False)

    activation_key = models.CharField(max_length=64, editable=False)

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return self.get_username()
    
    def get_short_name(self):
        return self.get_username()

    def get_masked_name(self):
        eun = self.email.split("@")[0]
        ed = ed = ".".join(self.email.lower().split('@')[1].split('.')[-2:])
        return "%s******%s-%s@%s" % (eun[0], eun[-1], crypto.GenSaltedHash(self.email)[:6], ed)

	def save(self, *args, **kwargs):
		if not self.id:
			self.activation_key = crypto.GenRandomHash()
		super(User, self).save(*args, **kwargs)

    REQUIRED_FIELDS = []

    objects = UserManager()

