from django.db import models
from django.contrib.auth.models import User
import gameshop.genre as game_genres #HUOM! 

class Score(models.Model):
    """ Model to keep all the scores in database """
    points = models.PositiveIntegerField()
    game = models.ForeignKey("Game", related_name="GameScores")
    user = models.ForeignKey(User, related_name="UserScores")

    class Meta:
        ordering = ["-points"]

class Game(models.Model):
    """ Model to keep all the game infromation in database """
    name = models.CharField(max_length=225, unique=True)
    description = models.CharField(max_length=300)
    release_date = models.DateField(auto_now_add=True)
    game_developer = models.ForeignKey(User, related_name="DeveloperGames")
    publisher = models.CharField(max_length=225, blank=True)
    # GENRE_CHOICES omassa tiedostossa
    genre = models.CharField(max_length=225, choices=game_genres.GENRE_CHOICES)
    source = models.URLField(max_length=225, unique=True)
    price = models.FloatField()

    def get_gamescores(self):
        return self.GameScores.all()
    leaderboard = property(get_gamescores)

    class Meta:
        ordering =["name"]

class Gamer(models.Model):
    """ Extend User model with user.developer field """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ManyToManyField("Game")


class Developer(models.Model):
    """ Extends User model with user.developer field """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def get_games(self):
        return self.user.DeveloperGames.all()
    inventory = property(get_games)
	
class GameSave(models.Model):
    gameState=models.CharField(max_length=2250)
    game=models.ForeignKey('Game')
    user=models.ForeignKey(User)
    saveTime=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["saveTime"]

