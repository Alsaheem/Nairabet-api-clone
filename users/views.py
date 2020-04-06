from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Profile,User
from .serializers import UserSerializer,ProfileSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing Profile instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileView(generics.ListCreateAPIView):
    """
    A viewset for viewing and editing Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A viewset for viewing and editing Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()