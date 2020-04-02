from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class League(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Bet(models.Model):
    HOME = 1
    DRAW = 2
    AWAY = 3
    OUTCOME = (
        (HOME, _('HOME to win')),
        (DRAW, _('DRAW by happen')),
        (AWAY, _('AWAY to win')),
    )
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    outcome = models.PositiveSmallIntegerField(
        choices=OUTCOME,
        default=HOME,
    )
    actual_outcome =  models.PositiveSmallIntegerField(
        choices=OUTCOME,
    )
    match_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=False)0
