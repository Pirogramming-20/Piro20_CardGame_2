from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random

# 유저 Profile 모델
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

# Game 모델
class Game(models.Model):

    # choice 처리
    attack_deck = sorted(random.sample(range(11), 5))
    defend_deck = sorted(random.sample(range(11), 5))

    attack_deck_tuple = [(n, n) for n in attack_deck]
    defend_deck_tuple = [(n, n) for n in defend_deck]

    attacker = models.ForeignKey(Profile,on_delete=models.CASCADE,
                                 related_name="attack",
                                 verbose_name="공격자")
    defender = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE,
                                 related_name="defend",
                                 verbose_name="수비자")
    attack_num = models.IntegerField(choices=attack_deck_tuple)
    defend_num = models.IntegerField(choices=defend_deck_tuple, null=True)

    rule = models.CharField("룰", max_length=10, null=True)

    winner = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               verbose_name="승리자", null=True)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} - {self.attacker.user.username} VS {self.defender.user.username}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)