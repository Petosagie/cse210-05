# Cycle Specification

> The best rides are the ones where you
> bite off much more than you can chew,
> and live through it.
> 
> &mdash; Doug Bradbury &mdash;


## Overview

---

Cycle is a game where the players try to cut each other off using cycles that leave a trail behind them.

## Rules

---

Cycle is played according to the following rules.

- Players can move up, down, left and right...
    - Player one moves using the W, S, A and D keys.
    - Player two moves using the I, K, J and L keys.
- Each player's trail grows as they move.
- Players try to maneuver so the opponent collides with their trail.
- If a player collides with their opponent's trail...
    - A "game over" message is displayed in the middle of the screen.
    - The cycles turn white.
    - Players keep moving and turning but don't run into each other.


## Project Structure

---

The project files and folders are organized as follows:

```
root                    (project root folder)
+-- CycleGame           (source code for game)
  +-- casting           (specific game classes)
  +-- directoring       (director class for game)
  +-- scripting         (utility game classes)
  +-- services          (services game classes)
  +-- shared            (game definition classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (constants for the program)
+-- design.png          (UML Class design)
+-- README.md           (general info)
```



## Requirements

---

Your program must also meet the following requirements.

- The program must include a README file.
- The program must include class and method comments.
- The program must have at least 16 classes.
- The program must remain true to game play described in the overview.


## By

- Osagie Ohenhen  -> petosagie@gmail.com

