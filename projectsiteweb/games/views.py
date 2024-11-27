from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response

from rest_framework import status
from rest_framework.views import APIView
from games.models import Game,Genre
from games.serializers import GameSerializer,GenreSerializer
# Create your views here.



class GameListApiView(APIView):
    """
    ´List´ or ´detail´ a game
    """
    
    def get_object(self,pk):
        try:
            return Game.objects.get(id=pk)
        except Game.DoesNotExist:
            raise Http404
        
    def get(self,request,pk=None):
        
        if pk == None:
            games_query = Game.objects.all()
            serializer_context = {'request':request}
            games_serialized = GameSerializer(games_query,many=True,context=serializer_context)
            return Response(games_serialized.data,status=status.HTTP_200_OK)
        else:
            game = self.get_object(pk=pk)
            serializer_context = {'request':request}
            game_serialized  = GameSerializer(game,context=serializer_context)
            return Response(game_serialized.data,status=status.HTTP_200_OK)
    
        
        

class GamePlatformListApiView(APIView):
    """
    `List` games by platform
    """
    
    def get_objects(self,platform,genre):
        try:
            if genre != None:
                return Game.objects.filter(platform=platform,genre__name=genre)
            return Game.objects.filter(platform=platform)
        except Game.DoesNotExist:
            raise Http404
    
    def get(self,request,platform,genre=None):
        
        games_by_platform = self.get_objects(platform=platform,genre=genre)
        serializer_context = {'request':request}
        games_serialized = GameSerializer(games_by_platform,many=True,context=serializer_context)
        return Response(games_serialized.data,status=status.HTTP_200_OK)



        