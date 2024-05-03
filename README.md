[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=14628162&assignment_repo_type=AssignmentRepo)

:warning: Everything between << >> needs to be replaced (remove << >> after replacing)

# << Project Title >>
## CS110 Final Project  << Semester, Year >>

## Team Members

Alex Santana

***

## Project Description

Create a 2D aracade game combining Lunar Landing, Asteroids, and sci-fi aspects like radar, space pirates, and fetch quests for an intresting game

New is just Asteroids, as previos was too complicated to integrate constant gravity, additional enemy ships to track and hunt you down, and moving from long distances in game was complicated
***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start menu
2. Dynamic (can move,shoot and interact) character
3. Obstacle collisions
4. Scrolling Background
5. Radar of potential threats
6. Dynamic (move and shoot) Enimes
7. Game over screen
8. Pause screen

Actual
1. Dynamic (can move,shoot and interact) character
2. Obstacle collisions
### Classes

- << You should have a list of each of your classes with a description >>

## ATP
Actual
| Step     |Procedure                                       |Expected Results                                               |
|----------|:----------------------------------------------:|--------------------------------------------------------------:|
|  1       | Run Program                                    | GUI window appears with background, starting at the main menu |
|  2       | Player clicks start or space bar               | GUI transitions to gameplay, starting the game                |
|  3       | Player presses either uparrow or w             | Player ship moveward, in its current direction                |
|  4       | Player presses either left arrow or a          | Player ship rotates counterclockwise                          |
|  5       | Player presses either right arrow or d         | Player ship rotates clockwise                                 |
|  6       | Player presses spacebar                        | Player ship shoots a laser beam                               |
|  7       | Player's ship collides into foreing objects    | Player ship explodes                                          |
|  8       | Player presses spacebar                        | Player ship shoots a laser beam                               |
|  9       | Enemy spaceship collides into foreign object   | Enemy ship explodes                                           |
|  10      | Asteriod collides into foreign object          | Foreign object explodes                                       |
|  11      | Player presses p                               | Game pauses                                                   |
|  12      | Laser beam collides into asteriod              | Asteriod breaks into smaller rocks                            |
|  13      | Player ship is destroyed                       | Player lives reduce by 1                                      |
|  14      | Player lives go into the negative              | Game ends, totaling the amount of time player has been alived for|

Sample
| Step                 |Procedure             |Expected Results                   |
|----------------------|:--------------------:|----------------------------------:|
|  1                   | Run Counter Program  |GUI window appears with count = 0  |
|  2                   | click count button   | display changes to count = 1      |
etc...
