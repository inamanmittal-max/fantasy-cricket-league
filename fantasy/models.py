
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Player(models.Model):
    ROLE_CHOICES = [
        ('BAT', 'Batsman'),
        ('BOWL', 'Bowler'),
        ('AR', 'All-Rounder'),
        ('WK', 'Wicket-Keeper'),
    ]

    name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    country = models.CharField(max_length=50)
    base_price = models.IntegerField()

    def __str__(self):
        return self.name


class FantasyTeam(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    budget_remaining = models.IntegerField(default=1000)

    def __str__(self):
        return self.name


class AuctionBid(models.Model):
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    bid_amount = models.IntegerField()

    def clean(self):
        # Rule 1: Bid must be >= base price
        if self.bid_amount < self.player.base_price:
            raise ValidationError(
                f"Bid must be at least {self.player.base_price}"
            )

        # Rule 2: Team must have enough budget
        if self.bid_amount > self.fantasy_team.budget_remaining:
            raise ValidationError(
                "Insufficient budget for this bid"
            )

    def save(self, *args, **kwargs):
        # Run validations
        self.clean()

        # Deduct budget only on first save
        if not self.pk:
            self.fantasy_team.budget_remaining -= self.bid_amount
            self.fantasy_team.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fantasy_team.name} → {self.player.name}"



class Match(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.name


class PlayerMatchStats(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)

    runs = models.IntegerField(default=0)
    wickets = models.IntegerField(default=0)
    catches = models.IntegerField(default=0)

    def total_points(self):
        return (
            self.runs * 1 +
            self.wickets * 20 +
            self.catches * 10
        )


class LeaderboardEntry(models.Model):
    fantasy_team = models.OneToOneField(FantasyTeam, on_delete=models.CASCADE)
    total_points = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.fantasy_team.name} - {self.total_points}"
