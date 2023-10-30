#!/usr/bin/env python

import curses
import time
import random
import shutil

# Initialize the screen
stdscr = curses.initscr()
# Do not display cursor
curses.curs_set(0)

# Initialize color pairs
curses.start_color()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

# Generate random positions for the "+" symbols
num_symbols = 500
width, height = shutil.get_terminal_size()
positions = []
for i in range(num_symbols):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    positions.append((x, y))

# Set the starting position, direction (1 for right, -1 for left), and speed of the pictures
pic_y, pic_x, pic_dir, pic_speed = 12, 0, 1, 2
pic2_y, pic2_x, pic2_dir, pic2_speed = 20, 30, -1, 2
pic3_y, pic3_x, pic3_dir, pic3_speed = 35, 15, -1, 1
pic4_y, pic4_x, pic4_dir, pic4_speed = 45, 40, 1, 1
alien1_y, alien1_x, alien1_dir, alien1_speed = 1, 60, 1, 1
ufo1_x, ufo1_y, ufo1_dir, ufo1_speed = 7, 3, 1, 1
planet_x, planet_y, planet_dir, planet_speed = 0, 2, 1, 1
planet_delay = 5  # Delay before the planet starts moving

ufo1 = r"""
       .-""`""-.
 ~~ _/`oOoOoOoOo`\_ ~~
~~ '.-=-=-=-=-=-=-.' ~~
 ~~  `-=.=-.-=.=-'  ~~
        ^  ^  ^       
"""

ufo2 = r"""
       .-""`""-.
  ~ _/`oOoOoOoOo`\_ ~
 ~ '.-=-=-=-=-=-=-.' ~
  ~  `-=.=-.-=.=-'  ~
        ^  ^  ^  
"""

pic = r""" 
        MMM8&&&.  
  _...MMMMM88&&&&..._
.::'''MMMMM88&&&&&&'''::.
::    MMMMM88&&&&&&    ::
'::...MMMMM88&&&&&&...::
  `''''MMMMM88&&&&''''`
        'MMM8&&&'
"""

pic2 = r""" 
   _..._
 .:::::::.
:::::::::::
:::::::::::
`:::::::::'
  `':::''
"""

pic3 = r"""
  \-/
 (@ @)
\ \-/
 \/ \
  \ /\
  _H_
"""

pic4 = r"""
  \-/
 (@ @)
\ \-/
 \/ \
  \ /\
  _H_
"""

alien1 = r"""
    .  .
     \/ 
    (@@)
 g/\_)(_/\e
g/\(=--=)/\e
    //\\
   _|  |_
"""

alien2 = r"""
     .  .
      \/ 
  g\ (@@) /e
 g\ \(_)/ /e
   \(=--=)/
     //\\
    _|  |_
"""

planet = r"""
                     .--------------.
                .---'  X        .    `---.
             .-'    .    X  .         .   `-.
          .-'     @@@@@@       .             `-.
        .'@@   @@@@@@@@@@@       @@@@@@@   .    `.
      .'@@@  @@@@@@@@@@@@@@     @@@@@@@@@         `.
     /@@@  X @@@@@@@@@@@@@@     @@@@@@@@@     X     \
    /        @@@@@@@@@@@@@@  @   @@@@@@@@@ @@     .  \
   /@  X      @@@@@@@@@@@   .  @@  @@@@@@@@@@@     @@ \
  /@@@      .   @@@@@@ X       @  @@@@@@@@@@@@@ X @@@@ \
 /@@@@@                  X .      @@@@@@@@@@@@@@  @@@@@ \
 |@@@@@    X    `.-./  .        .  @@@@@@@@@@@@@   @@@  |
/ @@@@@        --`-'       X        @@@@@@@@@@@ @@@    . \
|@ @@@@ .  X  X    `    @            @@      . @@@@@@    |
|   @@                         X    @@   .     @@@@@@    |
|  .     @   @ @       X              @@   X   @@@@@@.   |
\     @    @       @       .-.       @@@@       @@@      /
 |  @    @  @              `-'     . @@@@     .    .    |
 \ .  X       @  @@@@  .              @@  .           . /
  \      @@@    @@@@@@       .                   X     /
   \    @@@@@   @@\@@    /        X          .        /
    \ X  @@@       \ \  /  __        .   .     .--.  /
     \      .     . \.-.---                   `--'  /
      `.             `-'      .                   .'
        `.    X     / | `           X     .     .'
          `-.      /  |        X             .-'
             `-.          .         .     .-'
                `---.        .       .---'
                     `--------------'
"""

# Calculate the end time for the planet delay
planet_delay_end = time.time() + planet_delay

# Function to check if a position is empty
def is_position_empty(x, y):
    return stdscr.inch(y, x) == ord(' ')

# Function to draw pictures with transparency
def draw_picture_with_transparency(x, y, text, color_pair):
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            if 0 <= x + j < curses.COLS and 0 <= y + i < curses.LINES and (char != ' ' or is_position_empty(x + j, y + i)):
                stdscr.addch(y + i, x + j, char, curses.color_pair(color_pair) | curses.A_BOLD)

try:
    while True:
        # Clear the screen
        stdscr.clear()

        # Check if the planet delay has passed
        if time.time() >= planet_delay_end:
            # Move the planet picture
            planet_x += planet_dir * planet_speed

            # If the planet reaches the right border, change its direction to move left
            if planet_x + len(planet.split("\n")[0]) >= curses.COLS - 1:
                planet_dir = -1

            # If the planet reaches the left border, change its direction to move right
            if planet_x <= 0:
                planet_dir = 1

        # Display the planet picture with transparency
        draw_picture_with_transparency(planet_x, planet_y, planet, 4)

        # Display the "+" symbols
        for x, y in random.sample(positions, len(positions) // 2):
            stdscr.addstr(y, x, "+", curses.color_pair(2))

        # Display the "." symbols
        for x, y in random.sample(positions, len(positions) // 2):
            if random.random() < 0.5:
                stdscr.addstr(y, x, ".", curses.color_pair(2))
            else:
                stdscr.addstr(y, x, ".")

        # Move and display the other pictures with transparency
        draw_picture_with_transparency(pic_x, pic_y, pic, 2)
        draw_picture_with_transparency(pic2_x, pic2_y, pic2, 5)
        draw_picture_with_transparency(pic3_x, pic3_y, pic3, 3)
        draw_picture_with_transparency(pic4_x, pic4_y, pic4, 1)
        draw_picture_with_transparency(alien1_x, alien1_y, alien1 if alien1_dir == 1 else alien2, 1)
        draw_picture_with_transparency(ufo1_x, ufo1_y, ufo1 if ufo1_dir == 1 else ufo2, 2)

        # Move the pictures
        pic_x += pic_dir * pic_speed
        if pic_x <= 0 or pic_x + len(pic.split("\n")[0]) >= curses.COLS:
            pic_dir *= -1

        pic2_x += pic2_dir * pic2_speed
        if pic2_x <= 0 or pic2_x >= curses.COLS - 1:
            pic2_dir = -pic2_dir

        pic3_x += pic3_dir * pic3_speed
        if pic3_x <= 0 or pic3_x >= curses.COLS - 1:
            pic3_dir = -pic3_dir

        pic4_x += pic4_dir * pic4_speed
        if pic4_x <= 0 or pic4_x >= curses.COLS - 1:
            pic4_dir = -pic4_dir

        # Move the alien
        alien1_x += alien1_dir * alien1_speed
        if alien1_x <= 0 or alien1_x + 7 >= curses.COLS:
            alien1_dir = 1 if alien1_dir == -1 else -1

        # Swap the alien images
        alien1, alien2 = alien2, alien1

        # Move the UFO
        ufo1_x += ufo1_dir * ufo1_speed
        if ufo1_x <= 0 or ufo1_x + 7 >= curses.COLS:
            ufo1_dir = 1 if ufo1_dir == -1 else -1

        # Swap the UFO images
        ufo1, ufo2 = ufo2, ufo1

        # Refresh the screen
        stdscr.refresh()

        # Delay the loop for a short period
        curses.napms(100)

except KeyboardInterrupt:
    pass

finally:
    curses.endwin()

