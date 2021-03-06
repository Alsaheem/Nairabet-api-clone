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

class OutcomeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    #this allows us to be able to edit the bet
    class Meta:
        model = Outcome
        fields = [
            'id',
            'bet',
            'is_match_outcome'
        ]
        read_only_fields = ('bet',)
        #this allows us to makerefrence to a bet and not mess things up...check the doocs

class BetSerializer(serializers.HyperlinkedModelSerializer):
    home_team=serializers.SlugRelatedField(queryset=Team.objects.all(),slug_field='name')
    away_team=serializers.SlugRelatedField(queryset=Team.objects.all(),slug_field='name')
    outcomes = OutcomeSerializer(many=True)

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
            'outcomes'
        ]

    def create(self, validated_data):
        outcomes = validated_data.pop('outcomes')
        bet = Bet.objects.create(**validated_data)
        for outcome in outcomes:
            Outcome.objects.create(**outcome, bet=bet)
        return bet


class MyBetSerializer(serializers.ModelSerializer):
    # serializer for the mybets model
    outcomes = OutcomeSerializer(many=True)

    class Meta:
        ordering = ['-id']
        model = Mybet
        fields=('id','bets','stake','total_return','customer_id','is_won','outcomes')
        extra_kwargs = {'bets':  {'required':False}}

    def create(self, validated_data):
        print(validated_data['bets'])
        print(validated_data['outcomes'])
        outcomes = validated_data.pop('outcomes')
        picked_outcomes = []
        picked_bets = []
        bets= validated_data.get('bets')
        customer_id= validated_data['customer_id']
        stake= validated_data.get('stake')
        total_return= validated_data.get('total_return')
        mybet = Mybet.objects.create(customer_id=customer_id,stake=stake,total_return=total_return)
        for b in bets:
            mybet.bets.add(b)
            picked_bets.append(b.id)
        for outcome in outcomes:
            if "id" in outcome.keys():
                if Outcome.objects.filter(id=outcome["id"]).exists():
                    o = Outcome.objects.get(id=outcome["id"])
                    mybet.outcomes.add(o)
                    picked_outcomes.append(o.id)
                else:
                    continue
            else:
                continue

        return mybet


class BetcodeGeneratorSerializer(serializers.ModelSerializer):
    outcomes = OutcomeSerializer(many=True)
    class Meta:
        ordering = ['-id']
        model = GenerateBetcode
        fields=('id','bets','outcomes','bet_code','name')
        extra_kwargs = {'bets': {'required': False}}

    def create(self, validated_data):
        print(validated_data['bets'])
        print(validated_data)
        outcomes = validated_data.pop('outcomes')
        picked_outcomes = []
        picked_bets = []
        bets= validated_data.get('bets')
        name= validated_data.get('name')
        betcodegen = GenerateBetcode.objects.create(name=name)
        for b in bets:
            betcodegen.bets.add(b)
            picked_bets.append(b.id)
        for outcome in outcomes:
            if "id" in outcome.keys():
                if Outcome.objects.filter(id=outcome["id"]).exists():
                    o = Outcome.objects.get(id=outcome["id"])
                    betcodegen.outcomes.add(o)
                    picked_outcomes.append(o.id)
                else:
                    continue
            else:
                continue

        return betcodegen
