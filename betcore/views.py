from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,LeagueSerializer,TeamSerializer,BetSerializer,MyBetSerializer,BetcodeGeneratorSerializer,OutcomeSerializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.decorators import action
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

    @action(detail=True, methods=["GET"])
    def outomes(self, request, id=None):
        bet = self.get_object()
        outcomes = Outcome.objects.filter(bet=bet)
        serializer = OutcomeSerializer(outcomes, many=True)
        return Response(serializer.data, status=200)

    @action(detail=True, methods=["POST"])
    def outcome(self, request, id=None):
        bet = self.get_object()
        data = request.data
        data["bet"] = bet.id
        serializer = OutcomeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.erros, status=400)

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

    def perform_create(self, serializer):
        data = self.request.data
        print(data)
        customer_id = data["customer_id"]
        serializer.save(customer_id=customer_id)




class GenerateBetcodeViewSet(viewsets.ModelViewSet):
    """
    List all mybets, or create a new worker.
    """
    queryset = GenerateBetcode.objects.all()
    serializer_class = BetcodeGeneratorSerializer

