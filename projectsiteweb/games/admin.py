from django.contrib import admin
from games.models import Game,Genre
# Register your models here.

admin.site.register([Genre])

class GameModelAdmin(admin.ModelAdmin):

    readonly_fields = ["id"]
    
    
    


admin.site.register(Game,GameModelAdmin)