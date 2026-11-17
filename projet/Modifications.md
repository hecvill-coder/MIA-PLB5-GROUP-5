**Architecture \& New Files (artefactClass.py \& obstacleClass.py)**



New parent class Artefact (artefactClass.py): In the original version, Food directly managed the food object and its position.  this logic was extracted into a parent class Artefact



New obstacle files (obstacleClass.py): Added the Obstacle class (inheriting from Artefact) and its subclass Fence using "fence.gif".



**foodClass.py**



Inheritance: Food now inherits from Artefact instead of being a standalone class.



New food item: Added the Fish class ("blue", "fish.gif") for the penguin.



**animalClass.py**



New animal (Pinguin): Added the Pinguin class ("pinguin.gif", "blue") whose speed increases by +1 on "light blue" (water), decreases by -0.25 on "light green" (forest), and resets to 1 on all other terrain.



New method obstacle\_hit(): Added to the parent Animal class; it halves the speed (self.speed \*= 0.5) when an obstacle is hit.



Modification to Dog.adjust\_speed(): In the original version, the method simply contained pass. Added if/elif conditions (+= 0 / -= 0) and an else: self.speed = 1.



**animalRaceGame.py** 



New imports: Added Pinguin, Fish, and Fence.



Animal positions (create\_animals): Changed from 3 animals at Y-coordinates \[67, 0, -67] to 4 animals (monkey, dog, turtle\_racer, pinguin) at Y-coordinates \[75, 25, -25, -75].



Food items (create\_food\_items): Added Fish to food\_classes and updated the random Y-coordinates to \[75, 25, -25, -75].



New method create\_obstacle\_items(self, num\_items): Generates a list of Fence instances randomly distributed across the track and across the 4 lanes \[75, 25, -25, -75].



**main.py**



Execution path handling: Added import os and os.chdir(os.path.dirname(os.path.abspath(\_\_file\_\_))) at the beginning of initialize() to properly load the .gif files regardless of the directory from which the script is launched.



Shape registration: Added turtle.register\_shape() for "pinguin.gif", "fish.gif", and "fence.gif".



**Game parameters:**



Number of colored areas increased from 5 to 10.



Number of food items increased from 5 to 9.



Creation of 9 obstacles via obstacles = game.create\_obstacle\_items(9).



**Game loop (while):**



Added pinguin to the stopping condition, movement calls (pinguin.move(game.track)), debugging print statements, and final winner check (winners).



Food collisions: Added the if isinstance(food, Fish) block to double pinguin's speed.



Obstacle collisions: Added the nested loop for obstacle in obstacles: / for animal in \[pinguin, turtle\_racer, dog, monkey]: to apply animal.obstacle\_hit(), hide, and remove the fence.



raceTrackClass.py (vs raceTrackClass\_2.py)



No differences: Both files are strictly identical line for line.

