from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,LeagueSerializer,TeamSerializer,BetSerializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Category instances.
    """
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class LeagueViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing League instances.
    """
    serializer_class = LeagueSerializer
    queryset = League.objects.all()


class TeamViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Team instances.
    """
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

class BetViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Bet instances.
    """
    serializer_class = BetSerializer
    queryset = Bet.objects.all_bets()

class InPlayBets(APIView):
    """
    An apiView for viewing inplay Matches---currently playing matches.
    """
    def get(self,request):
        bets = Bet.objects.inplay()
        serializer = BetSerializer(bets,many=True,context={'request': request})
        return Response(serializer.data,status=200)