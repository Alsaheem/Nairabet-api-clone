# betcore serializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    # serializer for the category model
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'created_at']


class LeagueSerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the leagus model
    class Meta:
        model = League
        fields = ['id', 'name', 'description','category']

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    # serializer for the teams model
    class Meta:
        model = Team
        fields = ['id', 'name', 'description','league' ]