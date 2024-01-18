from django.db import models
import random
from ..user.models import User
from django.conf import settings
from allauth.socialaccount.models import SocialAccount

# Create your models here.


# 유저 Profile 모델
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_account = models.OneToOneField(SocialAccount,
                                          on_delete=models.CASCADE,
                                          null=True,
                                          blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


# Game 모델
class Game(models.Model):
    attack_deck = sorted(random.sample(range(11), 5))
    defend_deck = sorted(random.sample(range(11), 5))

    attack_deck_tuple = [(n, n) for n in attack_deck]
    defend_deck_tuple = [(n, n) for n in defend_deck]

    rule_choice = [("High", "High"), ("Row", "Row")]

    attacker = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE,
                                 related_name="attack",
                                 verbose_name="공격자")
    # related_name="attack" attacker 게임 불러올때(전적페이지)
    defender = models.ForeignKey(Profile,
                                 on_delete=models.CASCADE,
                                 related_name="defend",
                                 verbose_name="수비자")
    # related_name="defend" defender 게임 불러올때(전적페이지)
    attack_num = models.IntegerField(choices=attack_deck_tuple)
    defend_num = models.IntegerField(choices=defend_deck_tuple)

    rule = models.CharField("룰", choices=rule_choice, max_length=4)

    winner = models.ForeignKey(Profile,
                               on_delete=models.CASCADE,
                               verbose_name="승리자")

    def __str__(self):
        return f"{self.id} - {self.attacker.user.username} VS {self.defender.user.username}"
