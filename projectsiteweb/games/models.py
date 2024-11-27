from django.db import models
from django.core.validators import validate_comma_separated_integer_list
# Create your models here.


class GenreManager(models.Manager):
    
    def how_many_games_by_genre(self,name_genre):
        games = self.filter(name=name_genre)
        return (games.count,games)

class Genre(models.Model):
    name = models.CharField(max_length=100,unique=True)
    sorted_genres = GenreManager()
    
    
    def __str__(self):
        return self.name

class Game(models.Model):
    
    languages_available = {
        "EN":"English",
        "ES":"Spanish",
        "POR":"Portuguese",
        "FR":"French",
        "ITA":"Italian"
    }
    class Format(models.TextChoices):
        ISO = "ISO"
        WBFS = "WBFS"
        RGH = "RGH"

    class Platform(models.TextChoices):
        PC = "PC"
        XBOX = "XBOX360"
        PS4 = "PLAYSTATION 4"
        PS3 = "PLAYSTATION 3"
        PS2 = "PLAYSTATION 2"
        GBA = "GAMEBOY ADVANCE"
        NDS = "NINTENDO DS"
    
    image = models.URLField(verbose_name='image_game',null=True,blank=True)
    
    title = models.CharField(max_length=200,null=False,verbose_name="name game",unique=True,help_text="Name of game goes here")
    
    languages = models.CharField(max_length=100,null=False,default=languages_available.get("EN"),help_text="Here goes language of game")
    
    genre = models.ManyToManyField(to=Genre,related_name="genres",related_query_name="genre",)
    
    size = models.DecimalField(max_digits=100,decimal_places=2,null=False)
    
    format = models.CharField(choices=Format.choices,null=True,blank=True,max_length=100)
    
    platform = models.CharField(choices=Platform.choices,null=True,blank=True,max_length=100)
    
    version = models.CharField(max_length=10,blank=True,null=True)
    
    
    def __str__(self):
        genre_list = ", ".join([ i[1] for i in self.genre.values_list()])
        
        return f"{self.title} - {genre_list}"