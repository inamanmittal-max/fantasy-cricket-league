
from django.contrib import admin
from .models import (
    Player,
    FantasyTeam,
    AuctionBid,
    Match,
    PlayerMatchStats,
    LeaderboardEntry
)

admin.site.register(Player)
admin.site.register(FantasyTeam)
admin.site.register(AuctionBid)
admin.site.register(Match)
admin.site.register(PlayerMatchStats)
admin.site.register(LeaderboardEntry)
