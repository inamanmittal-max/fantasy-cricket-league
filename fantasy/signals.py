
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PlayerMatchStats, AuctionBid, LeaderboardEntry

@receiver(post_save, sender=PlayerMatchStats)
def update_leaderboard(sender, instance, **kwargs):
    player = instance.player

    try:
        # Find which fantasy team owns this player
        bid = AuctionBid.objects.get(player=player)
        fantasy_team = bid.fantasy_team
    except AuctionBid.DoesNotExist:
        return  # player not in any fantasy team

    # Calculate total points for this team
    total_points = 0

    bids = AuctionBid.objects.filter(fantasy_team=fantasy_team)

    for bid in bids:
        stats = PlayerMatchStats.objects.filter(player=bid.player)
        for s in stats:
            total_points += s.total_points()

    # Update or create leaderboard entry
    LeaderboardEntry.objects.update_or_create(
        fantasy_team=fantasy_team,
        defaults={"total_points": total_points}
    )
