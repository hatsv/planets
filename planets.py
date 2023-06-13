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

# Generate random positions for the "+" symbols
num_symbols = 300
width, height = shutil.get_terminal_size()
positions = []
for i in range(num_symbols):
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    positions.append((x, y))

# Set the starting position, direction (1 for right, -1 for left) and speed of the first picture
pic_y,pic_x,pic_dir,pic_speed = 12,0,1,2
pic2_y,pic2_x,pic2_dir,pic2_speed=20,curses.COLS -1,-1,2
pic3_y,pic3_x,pic3_dir,pic3_speed=35,curses.COLS -1,-1,1
alien1_y,alien1_x,alien1_dir,alien1_speed=30,0,1,1
ufo1_x, ufo1_y, ufo1_dir, ufo1_speed=7, 3, 1, 1

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
     .-o--.  
    :O o O :  
    : O. Oo;  
     `-.O-'     
"""

pic3 = r"""   
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
 g\ \_)(_/ /e  
   \(=--=)/   
     //\\      
    _|  |_    
"""

try:
    while True:
        # Clear the screen
        stdscr.clear()
        
        # Display the "+" symbols
        for x, y in random.sample(positions, len(positions)//2):
            stdscr.addstr(y, x, "+", curses.color_pair(2))

        # Display the "." symbols
        for x, y in random.sample(positions, len(positions)//2):
            if random.random() < 0.5:
                stdscr.addstr(y, x, ".", curses.color_pair(2))
            else:
                stdscr.addstr(y, x, ".")

        # Move the first picture
        pic_x += pic_dir * pic_speed
        if pic_x <= 0 or pic_x + len(pic.split("\n")[0]) >= curses.COLS:
            pic_dir *= -1

        # Display the first picture
        for i, line in enumerate(pic.split("\n")):
            if pic_x + len(line) > curses.COLS:
                break
            stdscr.addstr(pic_y + i, pic_x, line, curses.color_pair(2))

        # Move the second picture
        pic2_x += pic2_dir * pic2_speed
        if pic2_x <= 0 or pic2_x + len(pic2.split("\n")[0]) >= curses.COLS:
            pic2_dir *= -1

        # Display the second picture
        for i, line in enumerate(pic2.split("\n")):
            if pic2_x + len(line) > curses.COLS:
                break
            stdscr.addstr(pic2_y + i, pic2_x, line, curses.color_pair(4))

        # Move the third picture
        pic3_x += pic3_dir * pic3_speed
        if pic3_x <= 0 or pic3_x >= curses.COLS - 1:
            pic3_dir = -pic3_dir

        # Display the third picture
        for i, line in enumerate(pic3.split("\n")):
            if pic3_x + len(line) > curses.COLS:
                break
            stdscr.addstr(pic3_y + i, pic3_x, line, curses.color_pair(3))
            
        # Move the alien
        alien1_x += alien1_dir * alien1_speed
        if alien1_x <= 0 or alien1_x + 7 >= 80:
            alien1_dir = 1 if alien1_dir == -1 else -1

        # Display the alien
        current_alien1 = alien1 if alien1_dir == 1 else alien2
        for i, line in enumerate(current_alien1.split("\n")):
            stdscr.addstr(alien1_y + i, alien1_x, line, curses.color_pair(1))

        # Swap the alien images
        alien1, alien2 = alien2, alien1

        # Move the UFO
        ufo1_x += ufo1_dir * ufo1_speed
        if ufo1_x <= 0 or ufo1_x + 7 >= 80:
            ufo1_dir = 1 if ufo1_dir == -1 else -1

        # Display the UFO
        current_ufo1 = ufo1 if ufo1_dir == 1 else ufo2
        for i, line in enumerate(current_ufo1.split("\n")):
            stdscr.addstr(ufo1_y + i, ufo1_x, line)

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


 
