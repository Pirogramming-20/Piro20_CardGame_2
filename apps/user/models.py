from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
  profile_image = models.ImageField(
    "프로필 이미지", upload_to="user/profile", blank=True
  )
  short_description = models.TextField("소개글", blank=True)