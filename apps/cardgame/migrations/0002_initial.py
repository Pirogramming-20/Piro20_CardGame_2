# Generated by Django 5.0.1 on 2024-01-19 13:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cardgame', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='game',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack', to='cardgame.profile', verbose_name='공격자'),
        ),
        migrations.AddField(
            model_name='game',
            name='defender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defend', to='cardgame.profile', verbose_name='수비자'),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cardgame.profile', verbose_name='승리자'),
        ),
    ]
