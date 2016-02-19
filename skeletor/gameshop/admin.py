from django.contrib import admin
from .models import Game, Score, Gamer, Developer, GameSave
# Register your models here.

admin.site.register(Game)
admin.site.register(Gamer)
admin.site.register(GameSave)
admin.site.register(Developer)
admin.site.register(Score)
