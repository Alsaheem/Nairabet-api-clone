from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer,LeagueSerializer,TeamSerializer
from .models import Category,League,Team,Bet,Outcome,Mybet,GenerateBetcode

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