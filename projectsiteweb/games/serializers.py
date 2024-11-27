from rest_framework import serializers

from games.models import Game,Genre


class GameSerializer(serializers.HyperlinkedModelSerializer):
    
    
    url = serializers.HyperlinkedIdentityField(view_name="games_app:game-detail")
    class Meta:
        model = Game
        fields = ['id','image','title','languages','size','format','platform','url']
        
        


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Game
        fields = ['name','url']