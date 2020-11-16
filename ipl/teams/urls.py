from django.urls import path

from . import views

urlpatterns = [

    path('list/', views.team_list.as_view(), name='index'),
    path('add/', views.add_team.as_view(), name='index'),
    path('', views.index, name='index'),
]