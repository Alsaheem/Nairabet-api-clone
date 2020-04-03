from django.db import models
from django.contrib.auth.models import User
import string,random

# Create your models here.

#this is the model for the categories of diffrent leagues
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)

#this is the model for the leagues of diffrent teams with relationships  to various categories
class League(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

#this is the model for the diffrent teams possible with relationships to their various leagues
class Team(models.Model):
    name = models.CharField(max_length=100)
    League = models.ForeignKey(League,on_delete=models.CASCADE)
    description = models.TextField()


#this is the model for each single bet
class Bet(models.Model):
    # the home team of the match
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    # the away team of the match
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match_time = models.DateTimeField(auto_now_add=True)
    # to get if a match is playing curently
    is_currently_playing = models.BooleanField(default=False)
    # to get if a match is available for betting
    is_available_for_betting = models.BooleanField(default=False)

    @property
    def outcomes():
        return Bet.outcome_set.all()

#this is the model for the outcome of each single bet....more like choices to a poll
class Outcome(models.Model):
    option = models.CharField(max_length=50)
    bet = models.ForeignKey(Bet,on_delete=models.CASCADE,related_name = 'outcomes')
    # the odds of a particular outcome
    odd = models.IntegerField()
    # would be true when the match is played finish
    is_match_outcome = models.BooleanField(default=False)


#this is the model for the collection of bet that a person played or beton
class Mybet(models.Model):
    bets = models.ManyToManyField(Bet)
    stake = models.IntegerField()
    total_return = models.IntegerField()
    is_won = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


# function to generate a random value
def bet_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#this is the model for the bet code generator
class GenerateBetcode(models.Model):
    # this is the listof bets in the betslip
    bets = models.ManyToManyField(Bet)
    # this is the ammount staked on the list of bets
    stake = models.IntegerField()
    # this is the total return for the betslip
    total_return = models.CharField(max_length=10)
    # this is the betcode for the particular bet picked
    bet_code = models.IntegerField()

    def save(self, *args, **kwargs):
        self.bet_code = bet_code_generator()
        super(GenerateBetcode, self).save(*args, **kwargs)



