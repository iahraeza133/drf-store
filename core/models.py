from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
  email = models.EmailField(unique=True)
  USERNAME_FIELD = 'email'  # ورود با ایمیل
  REQUIRED_FIELDS = ['username']  # فیلدهای اجباری دیگر (نام کاربری)

  def __str__(self):
          return self.email