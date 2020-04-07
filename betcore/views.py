from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,LeagueSerializer,TeamSerializer,BetSerializer,MyBetSerializer,BetcodeGeneratorSerializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
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
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['match_time']

class InPlayBets(APIView):
    """
    An apiView for viewing inplay Matches---currently playing matches.
    """
    def get(self,request):
        bets = Bet.objects.inplay()
        serializer = BetSerializer(bets,many=True,context={'request': request})
        return Response(serializer.data,status=200)


class UserBets(APIView):
    """
    An apiView for viewing a user Bets
    """
    def get(self,request,user_id):
        mybets = Mybet.objects.filter(customer_id=user_id)
        serializer = MyBetSerializer(mybets,many=True,context={'request': request})
        return Response(serializer.data,status=200)

class MyBetViewSet(viewsets.ModelViewSet):
    """
    List all mybets, or create a new worker.
    """
    queryset = Mybet.objects.all()
    serializer_class = MyBetSerializer


class GenerateBetcodeViewSet(viewsets.ModelViewSet):
    """
    List all mybets, or create a new worker.
    """
    queryset = GenerateBetcode.objects.all()
    serializer_class = BetcodeGeneratorSerializer

