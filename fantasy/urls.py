from django.urls import path
from .views import home
from .views import (
    PlayerListView,
    FantasyTeamListView,
    AuctionBidCreateView,
    LeaderboardView
)

urlpatterns = [
    path('', home),
    path('players/', PlayerListView.as_view()),
    path('teams/', FantasyTeamListView.as_view()),
    path('auction/bid/', AuctionBidCreateView.as_view()),
    path('leaderboard/', LeaderboardView.as_view()),
]

