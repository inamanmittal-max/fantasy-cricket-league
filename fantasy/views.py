from rest_framework import generics
from .models import Player, FantasyTeam, AuctionBid, LeaderboardEntry
from .serializers import (
    PlayerSerializer,
    FantasyTeamSerializer,
    AuctionBidSerializer,
    LeaderboardSerializer
)
def home(request):
    return HttpResponse("Fantasy Cricket Backend is running")


class PlayerListView(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class FantasyTeamListView(generics.ListCreateAPIView):
    queryset = FantasyTeam.objects.all()
    serializer_class = FantasyTeamSerializer


class AuctionBidCreateView(generics.CreateAPIView):
    queryset = AuctionBid.objects.all()
    serializer_class = AuctionBidSerializer


class LeaderboardView(generics.ListAPIView):
    queryset = LeaderboardEntry.objects.order_by('-total_points')
    serializer_class = LeaderboardSerializer

from django.http import HttpResponse

