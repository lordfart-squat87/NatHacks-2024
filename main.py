import os
from time import sleep

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
    Displays navigation hint message centered in the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def main():
    HOME = 'Are You Ready to Take a DEEP Breath'
    current = HOME
    quit = False

    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)

        display_hint("Hold the Space Bar when you INHALE")
        action = input()

if __name__ == "__main__":
    main()
