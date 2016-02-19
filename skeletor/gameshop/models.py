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

    def __str__(self):
        return "{0}-{1}-{2}".format(self.game.name, self.user.username, self.points)

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

    def __str__(self):
        return self.name

class Gamer(models.Model):
    """ Extend User model with user.developer field """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ManyToManyField("Game")
    def addGame(self,game):
        self.library.add(game)
        sale=GameSale(user=self.user, game=game, gamePrice=game.price)
        sale.save()
        self.save()
    
    def __str__(self):
        return self.user.username


class Developer(models.Model):
    """ Extends User model with user.developer field """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def get_games(self):
        return self.user.DeveloperGames.all()
    inventory = property(get_games)

    def __str__(self):
        return self.user.username
	
class GameSave(models.Model):
    gameState=models.CharField(max_length=2250)
    game=models.ForeignKey('Game')
    user=models.ForeignKey(User)
    saveTime=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=["-saveTime"]
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.game.name, self.user.username, self.saveTime)

class GameSale(models.Model):
    user = models.ForeignKey(User)
    game=models.ForeignKey('Game')
    timeBought=models.DateTimeField(auto_now_add=True)
    gamePrice=models.FloatField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.game.name, self.user.username, self.timeBought)
