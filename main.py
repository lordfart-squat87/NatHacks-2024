#cd Downloads
#python test1.py

#maybe an asthma tester 
#
import os
import pygame
from time import sleep

pygame.init()

os.system("")  # enables ANSI characters in terminal

def clear_screen():
    '''
    Clears the terminal screen.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def print_header():
    '''
    Prints the header for the game in the center of the terminal.
    Input: N/A
    Returns: N/A
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[BREATHING GAME]"))

def display_current_site(current):
    '''
    Displays the current site name, centered under the header.
    Input:
        - current (str): current site
    Returns: N/A
    '''
    print("\033[2;32;40m{:^80}\033[0m".format(current))

def display_hint(message):
    '''
    Displays navigation hint message centered at the bottom of the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[24;0H\033[40;30;47m{:^80}\033[0m".format(message))

def main():
    HOME = 'Are You Ready to Take a DEEP Breath'
    current = HOME
    quit = False

    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)
        display_hint("Hold the Space Bar when you INHALE")

        # Initialize pygame window (not displayed but used for event loop)
        pygame.display.set_mode((1, 1))

        # Tracking variable for space bar hold
        space_held_start = None
        holding_space = False

        while not quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit = True

            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                if not holding_space:
                    # Start timing when space is first held
                    space_held_start = pygame.time.get_ticks()
                    holding_space = True

                # Check if 5 seconds have passed
                if holding_space and (pygame.time.get_ticks() - space_held_start >= 5000):
                    display_hint("Release the Space Bar!")
                    holding_space = False  # Reset holding status after prompt
            else:
                # Reset if the space bar is released
                space_held_start = None
                holding_space = False
                display_hint("Hold the Space Bar when you INHALE")

            pygame.time.delay(100)  # Add a short delay to control the loop speed

if __name__ == "__main__":
    main()
