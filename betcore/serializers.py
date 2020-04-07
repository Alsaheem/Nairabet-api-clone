# betcore serializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the category model

    leagues=serializers.HyperlinkedRelatedField(many=True,view_name='league-detail',read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'url',
            'name',
            'description',
            'created_at',
            'leagues'
            ]



class TeamSerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the teams model
    class Meta:
        model = Team
        fields = [
            'id',
            'url',
            'name',
            'description',
            'league'
            ]

class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the leagues model
    teams=TeamSerializer(many=True,read_only=True,)
    class Meta:
        model = League
        fields = [
            'id',
            'url',
            'name',
            'description',
            'category',
            'teams',
            ]

class BetSerializer(serializers.HyperlinkedModelSerializer):
    home_team=serializers.SlugRelatedField(queryset=Team.objects.all(),slug_field='name')
    away_team=serializers.SlugRelatedField(queryset=Team.objects.all(),slug_field='name')
    class Meta:
        model=Bet
        fields=[
            'id',
            'url',
            'match_time',
            'home_team',
            'away_team',
            'is_currently_playing',
            'is_available_for_betting',
        ]


class MyBetSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = Mybet
        fields=('id','bets','stake','total_return','customer_id','is_won')
        extra_kwargs = {'bets': {'required': False}}


class BetcodeGeneratorSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ['-id']
        model = GenerateBetcode
        fields=('id','bets','stake','total_return','bet_code')
        extra_kwargs = {'bets': {'required': False}}
