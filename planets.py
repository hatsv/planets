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
    curses.init_pair(6, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_WHITE, curses.COLOR_BLACK)
#    curses.init_pair(8, curses.COLOR_GRAY, curses.COLOR_BLACK)


def draw_picture_with_transparency(stdscr, x, y, text, color_pair):
    for i, line in enumerate(text.split("\n")):
        for j, char in enumerate(line):
            if 0 <= x + j < term_width and 0 <= y + i < term_height and (char != ' ' and char != '⠀' or is_position_empty(x + j, y + i)):
                stdscr.addch(y + i, x + j, char, curses.color_pair(color_pair) | curses.A_BOLD)

def is_position_empty(x, y):
    return stdscr.inch(y, x) == ord(' ')

try:
    stdscr = initialize_screen()
    initialize_colors()
    stdscr.timeout(100)  # Set a timeout for non-blocking input

    term_width, term_height = get_terminal_size(stdscr)

    num_symbols = 1500
    positions = []
    for i in range(num_symbols):
        x = random.randint(0, term_width - 1)
        y = random.randint(0, term_height - 1)
        positions.append((x, y))

    pic_y, pic_x, pic_dir, pic_speed = 12, 0, 1, 2
    pic2_y, pic2_x, pic2_dir, pic2_speed = 20, 30, -1, 2
    pic3_y, pic3_x, pic3_dir, pic3_speed = 35, 17, -1, 3
    pic4_y, pic4_x, pic4_dir, pic4_speed = 45, 40, 1, 1
    pic5_y, pic5_x, pic5_dir, pic5_speed = 40, 80, 1, 3
    pic6_y, pic6_x, pic6_dir, pic6_speed = 10, 1, 1, 3
    pic7_y, pic7_x, pic7_dir, pic7_speed = 40, 30, 1, 3
    pic8_y, pic8_x, pic8_dir, pic8_speed = 40, 170, 1, 3
    alien1_y, alien1_x, alien1_dir, alien1_speed = 1, 60, 1, 1
    ufo1_x, ufo1_y, ufo1_dir, ufo1_speed = 7, 3, 1, 1
    planet_x, planet_y, planet_dir, planet_speed = 40, 20, 1, 2
    planet2_x, planet2_y, planet2_dir, planet2_speed = 120, 5, 1, 2
    planet3_x, planet3_y, planet3_dir, planet3_speed = 70, 1, 1, 2
    planet_big_x, planet_big_y, planet_big_dir, planet_big_speed = 130, 2, 1, 1
    planet_big_delay = 1  # Delay before the planet starts moving

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

    pic5 = r""" 
    o   o
     )-(
    (O O)
     \=/
    .-"-.
   //\ /\\
 _// / \ \\_
=./ {,-.} \.=
    || ||
    || || 
  __|| ||__  
 `---" "---'  
    """

    pic6 = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠈⠉⠉⠛⠛⠷⢶⣤⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣿⣿⣿⣿⣷⣶⣦⣤⣄⡀⠈⠙⠻⣷⣦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⠿⠿⠛⠛⠛⠛⠻⠿⠿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠙⢿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣾⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⣿⣿⣿⣿⣷⡄⠀⠙⢿⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣿⣿⣿⣦⠀⠈⢿⣿⡄⠀⠀⠀⠀⠀
⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠒⠤⣄⣀⠀⠀⠀⠻⣿⣿⣿⣷⡀⠀⢿⣿⡀⠀⠀⠀⠀
⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣶⣶⣶⣶⣶⣦⣤⡀⠉⠳⣦⡀⠀⠘⣿⣿⣿⣧⠀⠈⣿⣇⠀⠀⠀⠀
⢰⠏⠀⠀⠀⠀⠀⠀⢀⠔⠀⣠⣴⣿⣿⡿⠛⠋⠉⠉⠉⠉⠙⠻⣿⣷⡀⠈⢷⡀⠀⠸⣿⣿⣿⡄⠀⢹⣿⠀⠀⠀⠀
⠏⠀⠀⠀⠀⠀⢀⡴⠃⢀⣼⣿⣿⠟⠁⠀⠀⡀⠀⢀⣠⣤⡤⣤⡈⢻⣿⡀⠘⣇⠀⠀⣿⣿⣿⡇⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡞⠀⢠⣿⣿⡿⠁⠀⢀⡴⠊⣠⡾⠋⠉⠀⠀⠀⡟⢈⣿⡇⢠⡟⠀⠀⣿⣿⣿⠃⠀⣸⡏⠀⠀⠀⠀
⠀⠀⠀⠀⢠⡟⠀⢀⣿⣿⡿⠀⠀⢠⡏⢠⣾⠏⢀⡠⢲⡖⢀⡜⠁⣼⡿⠀⣼⠃⠀⢰⣿⣿⡿⠀⢀⡿⠁⠀⠀⠀⠀
⠀⠀⠀⠀⣿⠃⠀⣼⣿⣿⡇⠀⢠⡿⠀⣾⡏⢀⡎⠀⠈⠉⠁⢀⣼⠟⢁⡼⠁⠀⢀⣾⣿⡿⠁⠀⡾⠁⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⣿⣿⣿⡇⠀⢸⡇⠀⣿⣧⠸⣧⣤⣤⣴⠾⠛⠁⠐⠁⠀⠀⣠⣾⣿⡟⠁⢀⡞⠁⠀⠀⠀⠀⠀⡄
⠀⠀⠀⢸⣿⠀⠀⣿⣿⣿⡇⠀⠈⣷⡀⠹⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⣿⡿⠋⢀⡴⠋⠀⠀⠀⠀⠀⠀⣰⠃
⠀⠀⠀⢸⣿⡄⠀⢹⣿⣿⣿⡀⠀⠘⢷⡄⠈⠻⢿⣿⣶⣶⣶⣶⣾⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀
⠀⠀⠀⠈⣿⣧⠀⠈⢿⣿⣿⣷⡄⠀⠀⠙⠳⠤⣀⣈⠉⠉⠙⠋⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠃⠀⠀
⠀⠀⠀⠀⠘⣿⣧⠀⠈⢿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⣿⣧⡀⠀⠻⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣾⡿⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠻⣿⣆⠀⠈⠻⢿⣿⣿⣿⣿⣶⣤⣄⣀⡀⠀⠀⠀⠀⢀⣀⣀⣤⣶⣾⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣦⣀⠀⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠷⣦⣤⣀⠀⠈⠉⠉⠙⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠒⠒⠒⠒⠒⠒⠒
    """

    pic7 = r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢠⢀⡐⢄⢢⡐⢢⢁⠂⠄⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⣌⠰⣘⣆⢧⡜⣮⣱⣎⠷⣌⡞⣌⡒⠤⣈⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⠱⡜⣞⣳⠝⣘⣭⣼⣾⣷⣶⣶⣮⣬⣥⣙⠲⢡⢂⠡⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⣑⢣⠝⣪⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣻⢦⣍⠢⢅⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⢆⡱⠌⣡⢞⣵⣿⣿⣿⠿⠛⠛⠉⠉⠛⠛⠿⢷⣽⣻⣦⣎⢳⣌⠆⡱⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠠⠌⢢⢃⡾⣱⣿⢿⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣏⠻⣷⣬⡳⣤⡂⠜⢠⡀⣀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⠂⣌⢃⡾⢡⣿⢣⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⡊⣿⣿⣾⣽⣛⠶⣶⣬⣭⣥⣙⣚⢷⣶⠦⡤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠂⠰⡌⡼⠡⣼⢃⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣾⡿⠿⣛⣯⡴⢏⠳⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠑⡌⠀⣉⣾⣩⣼⣿⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣠⣤⣤⣿⣿⣿⣿⡿⢛⣛⣯⣭⠶⣞⠻⣉⠒⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡶⢝⣢⣾⣿⣼⣿⣿⣿⣿⣿⣀⣼⣀⣀⣀⣤⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⠿⡛⠏⠍⠂⠁⢠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢀⢥⣰⣾⣿⣯⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣽⠟⣿⠐⠨⠑⡀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡐⢢⣟⣾⣿⣿⣟⣛⣿⣿⣿⣿⢿⣝⠻⠿⢿⣯⣛⢿⣿⣿⣿⡛⠻⠿⣛⠻⠛⡛⠩⢁⣴⡾⢃⣾⠇⢀⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠁⠊⠙⠉⠩⠌⠉⠢⠉⠐⠈⠂⠈⠁⠉⠂⠐⠉⣻⣷⣭⠛⠿⣶⣦⣤⣤⣴⣴⡾⠟⣫⣾⣿⡏⠀⠂⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢻⢿⢶⣤⣬⣉⣉⣭⣤⣴⣿⣿⡿⠃⠄⡈⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠘⢊⠳⠭⡽⣿⠿⠿⠟⠛⠉⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠈⠐⠀⠘⠀⠈⠀⠈⠀
    """

    pic8 = r"""⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⣀⠐⠀⠀⠂⠄⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠄⠀⠀⡐⠀⠀⠂⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⠂⠄⠒⡀⠀⠉⠁⠐⢀⠀⢊⠀⠄⠒⡀⢌⠀⠁⠂⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠄⠰⢈⠐⡈⡀⠄⠒⠈⠀⡄⡈⢠⡐⠠⢂⠠⠁⠄⠈⠐⠠⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠁⢀⠐⠈⠠⡐⢀⡀⠔⢡⢨⢱⡘⢤⡘⣄⡅⣱⢀⢂⠠⢄⠨⠀⠀⠀⠂⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⢀⠠⢀⠡⠀⠢⡄⠴⡡⢞⡮⣝⣮⣽⣲⢧⣵⢢⢌⡒⡈⣀⢀⠈⠀⠀⠀⠀⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠠⡁⠎⢁⠜⠴⣍⡣⢷⣿⣿⣿⣿⣿⣾⣽⡲⢌⡆⢆⠓⠌⢂⠀⠀⠀⠀⠃⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠰⠄⠀⡂⠇⠨⡄⡝⠳⣿⣿⣿⣿⣿⣿⣯⢷⡚⠜⡣⢭⡈⢄⠂⠀⡀⠀⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠔⠈⠰⠀⠱⠑⠘⢅⠟⣛⣿⢿⡟⣯⢳⢭⠱⣁⠇⠂⠄⠀⠀⠀⠀⢀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢈⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠉⢀⡐⠠⢌⠈⡈⢊⠘⠡⠛⠜⡸⠅⡊⡵⠌⢂⠡⢂⠁⠂⠐⠀⠀⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⡀⠀⠀⢂⡀⠆⠁⢠⠘⡄⠁⠊⠀⡑⢠⠀⢉⠢⢀⠀⠠⠐⠀⠀⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠄⠀⠁⠀⠀⠀⠨⠀⠈⡀⠀⠁⠀⠀⠁⠀⠀⠂⠠⠄⠃⠀⠠⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠂⠀⢈⠀⠈⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠂⠀⠀⠈⠀⠂⠀⠈⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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
             ,,,,,,
         o#'9MMHb':'-,o,
     .oH":HH$' "' ' -*R&o,
    dMMM*""'`'      .oM"HM?.
  ,MMM'          "HLbd< ?&H\
 .:MH ."\          ` MM  MM&b
. "*H    -        &MMMMMMMMMH:
.    dboo        MMMMMMMMMMMM.
.   dMMMMMMb      *MMMMMMMMMP.
.    MMMMMMMP        *MMMMMP .
 '    `#MMMMM           MM6P ,
  '    `MMMP"           HM*`,
   '    :MM             .- ,
    '.   `#?..  .       ..'
       -.   .         .-
         ''-.oo,oo.-''
    """

    planet2 = r"""
                                                                    ..;===+.
                                                                .:=iiiiii=+=
                                                             .=i))=;::+)i=+,
                                                          ,=i);)I)))I):=i=;
                                                       .=i==))))ii)))I:i++
                                                     +)+))iiiiiiii))I=i+:'
                                .,:;;++++++;:,.       )iii+:::;iii))+i='
                             .:;++=iiiiiiiiii=++;.    =::,,,:::=i));=+'
                           ,;+==ii)))))))))))ii==+;,      ,,,:=i))+=:
                         ,;+=ii))))))IIIIII))))ii===;.    ,,:=i)=i+
                        ;+=ii)))IIIIITIIIIII))))iiii=+,   ,:=));=,
                      ,+=i))IIIIIITTTTTITIIIIII)))I)i=+,,:+i)=i+
                     ,+i))IIIIIITTTTTTTTTTTTI))IIII))i=::i))i='
                    ,=i))IIIIITLLTTTTTTTTTTIITTTTIII)+;+i)+i`
                    =i))IIITTLTLTTTTTTTTTIITTLLTTTII+:i)ii:'
                   +i))IITTTLLLTTTTTTTTTTTTLLLTTTT+:i)))=,
                   =))ITTTTTTTTTTTLTTTTTTLLLLLLTi:=)IIiii;
                  .i)IIITTTTTTTTLTTTITLLLLLLLT);=)I)))))i;
                  :))IIITTTTTLTTTTTTLLHLLLLL);=)II)IIIIi=:
                  :i)IIITTTTTTTTTLLLHLLHLL)+=)II)ITTTI)i=
                  .i)IIITTTTITTLLLHHLLLL);=)II)ITTTTII)i+
                  =i)IIIIIITTLLLLLLHLL=:i)II)TTTTTTIII)i'
                +i)i)))IITTLLLLLLLLT=:i)II)TTTTLTTIII)i;
              +ii)i:)IITTLLTLLLLT=;+i)I)ITTTTLTTTII))i;
             =;)i=:,=)ITTTTLTTI=:i))I)TTTLLLTTTTTII)i;
           +i)ii::,  +)IIITI+:+i)I))TTTTLLTTTTTII))=,
         :=;)i=:,,    ,i++::i))I)ITTTTTTTTTTIIII)=+'
       .+ii)i=::,,   ,,::=i)))iIITTTTTTTTIIIII)=+
      ,==)ii=;:,,,,:::=ii)i)iIIIITIIITIIII))i+:'
     +=:))i==;:::;=iii)+)=  `:i)))IIIII)ii+'
   .+=:))iiiiiiii)))+ii;
  .+=;))iiiiii)));ii+
 .+=i:)))))))=+ii+
.;==i+::::=)i=;
,+==iiiiii+,
`+=+++;`
    """

    planet3 = r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡴⢧⣀⠀⠀⣀⣠⠤⠤⠤⠤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⠏⢀⡴⠊⠁⠀⠀⠀⠀⠀⠀⠈⠙⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢶⣶⣒⣶⠦⣤⣀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⠲⡌⠙⢦⠈⢧⠀
⠀⠀⠀⣠⢴⡾⢟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡴⢃⡠⠋⣠⠋⠀
⠐⠀⠞⣱⠋⢰⠁⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⠤⢖⣋⡥⢖⣫⠔⠋⠀⠀⠀
⠈⠠⡀⠹⢤⣈⣙⠚⠶⠤⠤⠤⠴⠶⣒⣒⣚⣩⠭⢵⣒⣻⠭⢖⠏⠁⢀⣀⠀⠀⠀⠀
⠠⠀⠈⠓⠒⠦⠭⠭⠭⣭⠭⠭⠭⠭⠿⠓⠒⠛⠉⠉⠀⠀⣠⠏⠀⠀⠘⠞⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⢤⣀⠀⠀⠀⠀⠀⠀⣀⡤⠞⠁⠀⣰⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⠿⠀⠀⠀⠀⠀⠈⠉⠙⠒⠒⠛⠉⠁⠀⠀⠀⠉⢳⡞⠉⠀⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """

    planet_big = r"""
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

    planet_big_delay_end = time.time() + planet_big_delay

    while True:
        stdscr.clear()

        for x, y in random.sample(positions, len(positions) // 2):
            stdscr.addstr(y, x, "+", curses.color_pair(2))

        for x, y in random.sample(positions, len(positions) // 2):
            if random.random() < 0.5:
                stdscr.addstr(y, x, ".", curses.color_pair(2))
            else:
                stdscr.addstr(y, x, ".")

        draw_picture_with_transparency(stdscr, planet2_x, planet2_y, planet2, 8)
        draw_picture_with_transparency(stdscr, planet3_x, planet3_y, planet3, 8)
        draw_picture_with_transparency(stdscr, pic6_x, pic6_y, pic6, 8)
        draw_picture_with_transparency(stdscr, pic7_x, pic7_y, pic7, 8)
        draw_picture_with_transparency(stdscr, pic8_x, pic8_y, pic8, 8)
        draw_picture_with_transparency(stdscr, pic_x, pic_y, pic, 2)
        draw_picture_with_transparency(stdscr, pic2_x, pic2_y, pic2, 5)
        draw_picture_with_transparency(stdscr, pic3_x, pic3_y, pic3, 3)
        draw_picture_with_transparency(stdscr, pic4_x, pic4_y, pic4, 4)
        draw_picture_with_transparency(stdscr, pic5_x, pic5_y, pic5, 6)
        draw_picture_with_transparency(stdscr, alien1_x, alien1_y, alien1 if alien1_dir == 1 else alien2, 6)
        draw_picture_with_transparency(stdscr, ufo1_x, ufo1_y, ufo1 if ufo1_dir == 1 else ufo2, 7)
        draw_picture_with_transparency(stdscr, planet_x, planet_y, planet, 1)

        term_width, term_height = get_terminal_size(stdscr)
        if time.time() >= planet_big_delay_end:
            planet_big_x += planet_big_dir * planet_big_speed

            if planet_big_x + len(planet_big.split("\n")[0]) >= term_width - 1:
                planet_big_dir = -1

            if planet_big_x <= 0:
                planet_big_dir = 1

        draw_picture_with_transparency(stdscr, planet_big_x, planet_big_y, planet_big, 4)


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

        pic5_x += pic5_dir * pic5_speed
        if pic5_x <= 0 or pic5_x >= term_width - 1:
            pic5_dir = -pic5_dir

        planet_x += planet_dir * planet_speed
        if planet_x <= 0 or planet_x >= term_width - 1:
            planet_dir = -planet_dir

        alien1_x += alien1_dir * alien1_speed
        if alien1_x <= 0 or alien1_x + 7 >= term_width:
            alien1_dir = 1 if alien1_dir == -1 else -1

        alien1, alien2 = alien2, alien1

        ufo1_x += ufo1_dir * ufo1_speed
        if ufo1_x <= 0 or ufo1_x + 7 >= term_width:
            ufo1_dir = 1 if ufo1_dir == -1 else -1

        ufo1, ufo2 = ufo2, ufo1

        stdscr.refresh()

        time.sleep(0.09)

except KeyboardInterrupt:
    cleanup(stdscr)

except Exception as e:
    cleanup(stdscr)
    raise e

