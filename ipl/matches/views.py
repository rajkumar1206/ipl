from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import AllowAny
from .models import Matches, IPLSeason
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core import serializers
import json
from django.forms.models import model_to_dict
from teams.models import Team

@api_view(['GET', 'POST'])
def index(request):
    return Response({"data": "This is the body field..."}, status=200)



class matches_list(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        try:
            data = serializers.serialize(
                "json", Matches.objects.all())
            json_data = {"status": "success", "data": json.loads(data)}
            return Response(json_data)
        except:
            return Response({"status": "failed"}, status=404)



class add_match(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        try:
            print(request.data)
            data = request.data

            ipl = IPLSeason.objects.get(pk=2020)
            team1 = Team.objects.get(pk=data["team_one"])
            team2 = Team.objects.get(pk=data["team_two"])
            toss = Team.objects.get(pk=data["toss"])
            match_won = Team.objects.get(pk=data["match_won"])

            print(data["elected"].upper()[0])
            match = Matches(year=ipl, team_one=team1, team_two=team2, toss=toss, elected=data["elected"].upper()[0], first_inning_score=data["first_inning_score"], second_inning_score=data["second_inning_score"], first_inning_over=data["first_inning_over"], second_inning_over=data["second_inning_over"], match_won=match_won )
            match.save()

            Team.objects.filter(pk=data["team_one"]).update(total_matches=data["new_total_matches_1"], wins=data["new_wins_1"], losses=data["new_losses_1"], points=data["new_points_1"], nrr=data["new_nrr_1"])
            Team.objects.filter(pk=data["team_two"]).update(total_matches=data["new_total_matches_2"], wins=data["new_wins_2"], losses=data["new_losses_2"], points=data["new_points_2"], nrr=data["new_nrr_2"])

            return Response({"status": "success"}, status=201)
        except AttributeError:
            return Response({"status": "failed", "err_message": "Please enter the valid attribute credential"}, status=403)
        except ValueError:
            return Response({"status": "failed", "err_message": "Please enter the valid credential"}, status=403)
