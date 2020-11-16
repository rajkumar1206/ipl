from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.matches_list.as_view(), name='index'),
    path('add/', views.add_match.as_view(), name='index'),
    path('', views.index, name='index'),
]