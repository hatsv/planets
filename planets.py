#!/usr/bin/env python

import curses
import time
import random

def get_terminal_size(stdscr):
    term_height, term_width = stdscr.getmaxyx()
    return term_width, term_height

def initialize_screen():
    stdscr = curses.initscr()
    # Do not display cursor
    curses.curs_set(0)
    return stdscr

def cleanup(stdscr):
    curses.endwin()
    exit(0)

def initialize_colors():
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

def draw_picture_with_transparency(stdscr, x, y, text, color_pair):
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            if 0 <= x + j < term_width and 0 <= y + i < term_height and (char != ' ' or is_position_empty(x + j, y + i)):
                stdscr.addch(y + i, x + j, char, curses.color_pair(color_pair) | curses.A_BOLD)

def is_position_empty(x, y):
    return stdscr.inch(y, x) == ord(' ')

try:
    stdscr = initialize_screen()
    initialize_colors()
    stdscr.timeout(100)  # Set a timeout for non-blocking input

    term_width, term_height = get_terminal_size(stdscr)

    num_symbols = 500
    positions = []
    for i in range(num_symbols):
        x = random.randint(0, term_width - 1)
        y = random.randint(0, term_height - 1)
        positions.append((x, y))

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
         \  _.-'~~~~'-._   /
         .-~ \__/  \__/ ~-.
       .-~   (oo)  (oo)    ~-.
      (_____//~~\\//~~\\______)
 _.-~`                         `~-.
/O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O=O\
\___________________________________/
           \x x x x x x x/
            \x_x_x_x_x_x/
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
     g\ \ )( / /e
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

    planet_delay_end = time.time() + planet_delay

    while True:
        stdscr.clear()

        term_width, term_height = get_terminal_size(stdscr)
        if time.time() >= planet_delay_end:
            planet_x += planet_dir * planet_speed

            if planet_x + len(planet.split("\n")[0]) >= term_width - 1:
                planet_dir = -1

            if planet_x <= 0:
                planet_dir = 1

        draw_picture_with_transparency(stdscr, planet_x, planet_y, planet, 4)

        for x, y in random.sample(positions, len(positions) // 2):
            stdscr.addstr(y, x, "+", curses.color_pair(2))

        for x, y in random.sample(positions, len(positions) // 2):
            if random.random() < 0.5:
                stdscr.addstr(y, x, ".", curses.color_pair(2))
            else:
                stdscr.addstr(y, x, ".")

        draw_picture_with_transparency(stdscr, pic_x, pic_y, pic, 2)
        draw_picture_with_transparency(stdscr, pic2_x, pic2_y, pic2, 5)
        draw_picture_with_transparency(stdscr, pic3_x, pic3_y, pic3, 3)
        draw_picture_with_transparency(stdscr, pic4_x, pic4_y, pic4, 1)
        draw_picture_with_transparency(stdscr, alien1_x, alien1_y, alien1 if alien1_dir == 1 else alien2, 1)
        draw_picture_with_transparency(stdscr, ufo1_x, ufo1_y, ufo1 if ufo1_dir == 1 else ufo2, 2)

        pic_x += pic_dir * pic_speed
        if pic_x <= 0 or pic_x + len(pic.split("\n")[0]) >= term_width:
            pic_dir *= -1

        pic2_x += pic2_dir * pic2_speed
        if pic2_x <= 0 or pic2_x >= term_width - 1:
            pic2_dir = -pic2_dir

        pic3_x += pic3_dir * pic3_speed
        if pic3_x <= 0 or pic3_x >= term_width - 1:
            pic3_dir = -pic3_dir

        pic4_x += pic4_dir * pic4_speed
        if pic4_x <= 0 or pic4_x >= term_width - 1:
            pic4_dir = -pic4_dir

        alien1_x += alien1_dir * alien1_speed
        if alien1_x <= 0 or alien1_x + 7 >= term_width:
            alien1_dir = 1 if alien1_dir == -1 else -1

        alien1, alien2 = alien2, alien1

        ufo1_x += ufo1_dir * ufo1_speed
        if ufo1_x <= 0 or ufo1_x + 7 >= term_width:
            ufo1_dir = 1 if ufo1_dir == -1 else -1

        ufo1, ufo2 = ufo2, ufo1

        stdscr.refresh()

        time.sleep(0.1)

except KeyboardInterrupt:
    cleanup(stdscr)

except Exception as e:
    cleanup(stdscr)
    raise e

