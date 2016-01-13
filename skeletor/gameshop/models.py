from django.db import models
import genre as game_genres #HUOM!

class Score(models.Model):
	"""Model to keep all the scores in database"""
	
	points = models.PositiveIntegerField()
	game = models.ForeignKey(Game, related_name="GameScores")
	user = models.ForeignKey(User, related_name="UserScores")
	
	class Meta:
		ordering = ["points"]

class Game(models.Model):
	"""Model to keep all the game infromation in database"""
	
	name = models.CharField(max_length=225)
	description = models.CharField(max_length=300)
	release_date = models.DateField(blank=True)
	developer = models.ForeignKey(User, related_name="DeveloperGames")
	publisher = models.CharField(max_length=225, blank=True)
	genre = models.CharField(max_length=225, choices=game_genres.GENRE_CHOICES) #GENRE_CHOICES omassa tiedostossa
	source = models.URLField(max_length=225)

	def get_gamescores(self):
		return self.DeveloperGames.all()
	leaderboard = property(get_gamescores)

	class Meta:
		ordering =["name"]

class User(models.Model):
	"""Model to keep all the user infromation in database"""
	
	name = models.CharField(max_length=225)
	user_name = models.CharField(max_length=225)
	email = models.EmailField(max_length=225)
	date_of_birth = models.DateField()
	library = models.ManyToManyField(Game)

	

	"""def is_developer(self):
		if not self.DeveloperGames.all():
			return False
		else:
			return True """
			
