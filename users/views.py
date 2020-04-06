from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Profile,User
from .serializers import UserSerializer,ProfileSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

class ProfileView(generics.ListCreateAPIView):
    """
    An APIView for viewing and creating Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class ProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    An APIView for viewing Profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()