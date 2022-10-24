# Fireball
It's Harry's turn to compete in the first task! He is up against the Hungarian Horntail and its fiery breath. 
Fireball is a game where the player tries to avoid fireballs to keep playing. 

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cycle
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                                  (project root folder)
+-- fireball-dodge                    (source code for game)
  +-- game                            (specific game classes)
    +-- casting
      +-- actor.py
      +-- cast.py
      +-- fireball.py
    +-- directing
      +-- director.py
    +-- services
      +-- keyboard_service.py
      +-- video_service.py
    +-- shared
      +-- color.py
      +-- point.py
  +-- __main__.py                     (entry point for program)
  +-- constants.py                    (common variables)
+-- README.md                         (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Amanda Stokes sto20001@byui.edu