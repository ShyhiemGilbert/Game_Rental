from django.urls import path
from . import views  # . means in current directory
from . import apps


app_name = 'games'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:game_id>', views.detail, name='detail')  # games/1
    #              /game/1
]
