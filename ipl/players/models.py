from django.db import models
from teams.models import Team

# Create your models here.
class Player(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    date_of_birth = models.DateField(null=False)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, default="", null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name