from rest_framework import serializers
from .models import Player, FantasyTeam, AuctionBid, LeaderboardEntry


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class FantasyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantasyTeam
        fields = ['id', 'name', 'budget_remaining']


class AuctionBidSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuctionBid
        fields = '__all__'


class LeaderboardSerializer(serializers.ModelSerializer):
    fantasy_team = serializers.StringRelatedField()

    class Meta:
        model = LeaderboardEntry
        fields = ['fantasy_team', 'total_points']
