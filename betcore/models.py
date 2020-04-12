from django.db import models
from django.contrib.auth.models import User
import string,random

# Create your models here.

#this is the model for the categories of diffrent leagues
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)

#this is the model for the leagues of diffrent teams with relationships  to various categories
class League(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name="leagues",on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.name)


#this is the model for the diffrent teams possible with relationships to their various leagues
class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, related_name="teams",on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return "{}".format(self.name)

class BetManager(models.Manager):
    def all_bets(self):
        return super().get_queryset()

    def inplay(self):
        # this gives all the bets that are currently playing...ie matches that are currently playing
        return super().get_queryset().filter(is_currently_playing=True)

#this is the model for each single bet
class Bet(models.Model):
    # the home team of the match
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name = 'home_teams')
    # the away team of the match
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE,related_name = 'away_teams')
    match_time = models.DateTimeField(auto_now_add=True)
    # to get if a match is playing curently
    is_currently_playing = models.BooleanField(default=False)
    # to get if a match is available for betting
    is_available_for_betting = models.BooleanField(default=False)

    objects = BetManager()

    # This is not necessary anymore since there's a related name
    # argument on thr foreign key relationsip

    # @property
    # def outcomes():
    #     return Bet.outcome_set.all()

    def __str__(self):
        return "{}--vs--{}".format(self.home_team,self.away_team)

#this is the model for the outcome of each single bet....more like choices to a poll
class Outcome(models.Model):
    option = models.CharField(max_length=50)
    bet = models.ForeignKey(Bet,on_delete=models.CASCADE,related_name = 'outcomes')
    # the odds of a particular outcome
    odd = models.IntegerField()
    # would be true when the match is played finish
    is_match_outcome = models.BooleanField(default=False)

    def __str__(self):
        return "{}--{} odds".format(self.option,self.odd)


#this is the model for the collection of bet that a person played or beton
class Mybet(models.Model):
    bets = models.ManyToManyField(Bet,related_name='mybet_bets')
    outcomes = models.ManyToManyField(Outcome,related_name='mybet_outcomes')
    stake = models.IntegerField()
    total_return = models.IntegerField()
    is_won = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{}--winner={}".format(self.customer.username,self.is_won)


# function to generate a random value
def bet_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

#this is the model for the bet code generator
class GenerateBetcode(models.Model):
    # this is the listof bets in the betslip
    bets = models.ManyToManyField(Bet)
    outcomes = models.ManyToManyField(Outcome,related_name='bet_gen_outcomes')
    bet_code = models.CharField(blank=True, null=True,max_length=6)

    def save(self, *args, **kwargs):
        self.bet_code = bet_code_generator()
        super(GenerateBetcode, self).save(*args, **kwargs)

    def __str__(self):
        return "Betcode {}--to return {}".format(self.bet_code,self.total_return)

