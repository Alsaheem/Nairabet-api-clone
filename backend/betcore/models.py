from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)

class League(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Bet(models.Model):
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match_time = models.DateTimeField(auto_now_add=True)
    is_currently_playing = models.BooleanField(default=False)
    is_available_for_betting = models.BooleanField(default=False)

    @property
    def outcomes():
        return Bet.outcome_set.all()

class Outcome(models.Model):
    option = models.CharField(max_length=50)
    bet = models.ForeignKey(Bet,on_delete=models.CASCADE,related_name = 'outcomes')
    odd = models.IntegerField()
    is_match_outcome = models.BooleanField(default=False)


class Mybet(models.Model):
    bets = models.ManyToManyField(Bet)
    stake = models.IntegerField()
    total_return = models.IntegerField()
    is_won = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class GenerateBetcode(models.Model):
    bets = models.ManyToManyField(Bet)
    stake = models.IntegerField()
    total_return = models.CharField(max_length=10)
    bet_code = models.IntegerField()

    def save(self, *args, **kwargs): 
        self.bet_code = bet_code_generator()
        super(GenerateBetcode, self).save(*args, **kwargs)



