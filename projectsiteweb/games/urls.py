from django.urls import path
from games.views import GameListApiView,GamePlatformListApiView

app_name = "games_app"

urlpatterns = [
    path('all-games/',GameListApiView.as_view(),name='game-list'),
    path('all-games/<int:pk>/',GameListApiView.as_view(),name='game-detail'),
    path('all-games/<str:platform>/',GamePlatformListApiView.as_view(),name='game_platform-list'),
    path('all-games/<str:platform>/<str:genre>/',GamePlatformListApiView.as_view(),name='game_platform_genre-list')
]