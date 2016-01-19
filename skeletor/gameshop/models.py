from django.db import models
from django.contrib.auth.models import User
import gameshop.genre as game_genres #HUOM!

class Score(models.Model):
	"""Model to keep all the scores in database"""
	
	points = models.PositiveIntegerField()
	game = models.ForeignKey("Game", related_name="GameScores")
	user = models.ForeignKey(User, related_name="UserScores")
	
	class Meta:
		ordering = ["points"]

class Game(models.Model):
	"""Model to keep all the game infromation in database"""
	
	name = models.CharField(max_length=225, unique=True)
	description = models.CharField(max_length=300)
	release_date = models.DateField(blank=True)
	game_developer = models.ForeignKey(User, related_name="DeveloperGames") # can't be just developer because it clashes with Developer.library
	publisher = models.CharField(max_length=225, blank=True)
	genre = models.CharField(max_length=225, choices=game_genres.GENRE_CHOICES) #GENRE_CHOICES omassa tiedostossa
	source = models.URLField(max_length=225, unique=True)

	def get_gamescores(self):
		return self.DeveloperGames.all()
	leaderboard = property(get_gamescores)

	class Meta:
		ordering =["name"]

class Gamer(models.Model):
	"""Model to keep all the gamer infromation in database"""
	user = models.ForeignKey(User)
	#date_of_birth = models.DateField()
	library = models.ManyToManyField("Game")


class Developer(models.Model):
	"""Model to keep all the developer infromation in database"""
	user = models.ForeignKey(User)
	#date_of_birth = models.DateField()
	library = models.ManyToManyField("Game")

	
