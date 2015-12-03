Project Plan
============

1. Team
-------
350446 Amin Modabberian
355810 Johannes Kaunisvaara
355153 Matti Yli-Ojanperä

2. Goal
-------
Our first Goal for the project is to create an online game store for JavaScript games. The service has two types of users: players and developers. Developers can add their games to the service and set a price for it. Players can buy games on the platform and then play purchased games online.

Our second goal is to improve our skills in web software developing and team work.


3. Plans
--------
### URL layout ###
index.html - The main page
register.html - User and developer registration
profile.html - User profile for developers and gamers
shop.html - List of games in shop
play.html - Page for selected game for playing
404.html - Customized 404 page

### Additional features ###
Mobile friendly (Bootstrap)
Social media sharing
Third party login
Save/load and resolution feature
Own game

### Django models ###
* user
    + Basic information of user(Name, email etc.)
    + Information whether the user is developer or gamer
    + List of games the user has bought
    + List of games the user has developed
* game
    + Basic information of game(Name, developer etc.)
    + Leaderboard
    + source

4. Process and Time Schedule
----------------------------

* Week 50
	+ Start project plan

* Week 51
	+ Finish project plan

* Week 52
	+ Holidays

* Week 53
	+ Holidays

* Week 1
	+ Creation of Django project
	+ Authentication
		- First draft of templates
	+ Creation of models
		- Basic player functionalities 
			+ First draft of templates
			
		- Basic developer functionalities 
			+ First draft of templates
			

* Week 2
	+ Authentication
		- Email confirmation
	+ Basic player functionalities 
		- Finishing models
		- Begin testing player functionalities
	+ Basic developer functionalities 
		- Finishing models
		- Begin testing developer functionalities

* Week 3
	+ Game/service interaction
	+ Continuing unit tests

* Week 4
	+ Security proofing
	+ Finish unit tests
	
* Week 5
	+ Visual appearance CSS / Bootsrap 
	+ Additional Features
		- Mobile Friendly
		- Social media Sharing

* Week 6
	+ Additional Features
		- Third party login
		- Save/Load and resolution feature

* Week 7
	+ Final testing round
	+ Finishing project 
	+ Own Game?

* Deadlines
    * Group registration - 13.12.2015 midnight
    * Project Plan - 20.12.2015 midnight
    * Final submission - 20.2.2016 midnight (end of period III)
    * Project demonstrations - few weeks after submission, announced when space has been reserved

5. Testing
----------
Backend is tested by unit tests.
Frontend is tested by hand or if we have time, we use robot framework 
for automated tests

Testing will be done in every step of implementation and can be seen in schedule. We have reserved also week 4 and week 7 for testing.

6. Risk Analysis
----------------
Week 4 is reserved for security proofing. We are concentrated to prevent manipulating scrores in games, getting games without payment and profile security.


