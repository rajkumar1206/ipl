from django.db import models

# Create your models here.
class Team(models.Model):
    team_name = models.CharField(max_length=30, primary_key=True)
    team_color = models.CharField(max_length=30, default="white")
    total_matches = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    nrr = models.FloatField(default=0.0)

    def __str__(self):
        return self.team_name

    class Meta:
        ordering = ['-points', '-nrr']