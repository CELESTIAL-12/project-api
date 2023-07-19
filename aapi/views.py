#from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from django.http import HttpResponse,JsonResponse,HttpResponse
from django.views.generic import ListView,DetailView,TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import MovieSerializer,MovieMiniSerializer
from .models import Movie
from rest_framework.response import Response

# Movies = {"Movies1": "WAR", select_ip = "0.0.0.0:"+str(port)}

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



    def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)    
        return Response(serializer.data)