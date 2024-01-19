from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import random

# 유저 Profile 모델
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# Game 모델
class Game(models.Model):

    attacker = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                 related_name="attack",
                                 verbose_name="공격자")
    defender = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE,
                                 related_name="defend",
                                 verbose_name="수비자")
    attack_num = models.IntegerField()
    defend_num = models.IntegerField(default=None, null=True)

    rule = models.CharField("룰", max_length=10, null=True)

    winner = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               verbose_name="승리자", null=True)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.attacker.user.username} VS {self.defender.user.username}"

user = get_user_model()
@receiver(post_save, sender=user)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile_social(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
