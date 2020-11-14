from django.db import models

from teams.models import Team

# Create your models here.
class IPLSeason(models.Model):
    season = models.IntegerField(default=2020, primary_key=True)

    def __str__(self):
        return str(self.season) + ' season'


class Matches(models.Model):

    options = (
        ('B', 'BAT'),
        ('F', 'FIELD'),
    )

    year = models.ForeignKey(IPLSeason, on_delete=models.CASCADE, default=2020)
    match_no = models.AutoField(primary_key=True)
    team_one = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name="team_one", default="")
    team_two = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name="team_two", default="")
    toss = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False, related_name="toss", default="")
    elected = models.CharField(max_length=1, choices=options)
    first_inning_score = models.IntegerField(blank=False)
    first_inning_over = models.FloatField(blank=False)
    second_inning_score = models.IntegerField(blank=False)
    second_inning_over = models.FloatField(blank=False)
    match_won = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="match_won", default="")

    def __str__(self):
        return str(self.match_no) + ' ' + str(self.team_one) + ' vs ' + str(self.team_two)