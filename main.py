import os
import time


#this will seve as main game logic

os.system("")  # enables ANSI characters in terminal

def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def display_error(error):
    '''
    Displays an error message under the current site as specificed by "error".
    Input:
        - error (str): error message to display
    Returns: N/A
    '''
    move_cursor(0, 3)
    print("\033[6;31;40m{:^80}\033[0m".format(error))
    sleep(0.6)
    clear_screen()

def print_header():
    '''
    Prints the BROWSE-175 header.
    Input: N/A
    Returns: N/A 
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[ BROWSE-175 ]"))

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def display_current_site(current):
    '''
    Displays the current site underneath the header.
    Input:
        - current (str): current site
    Returns: N/A
    '''
    print("\033[2;32;40m{:^80}\033[0m".format("Currently viewing: " + current))
    print("\033[4;30;40m{:^80}\033[0m".format(""))

def display_hint(message):
    '''
    Displays navigation hint message in the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def display_buttons(back, fwd):
    '''
    Displays the navigational buttons at the top of the terminal.
    "(<) BACK" and "FORWARD (>)" labels should only be displayed
    if there are sites to go back or forward to.
    Input: 
        - back: stack of previous sites
        - fwd: stack of forward sites
    Returns: N/A
    '''
    if not fwd.isEmpty():
        print_location(71, 3,  "FORWARD (>)")
    if not back.isEmpty():
        print_location(0, 3,  "BACK (<)")
    

def goToNewSite(current, bck, fwd):
    '''
    goToNewSite pushes the current site to the back stack and the new string which is promted will be a new URL that the user inputs  and this is becomes the new current location of the site; it displays a prompt that asks the user for a URL to enter
    Inputs:current, bck, fwd
    Returns:current which is just the current location of the sites
    '''
    bck.push(current)

    URL = str(input('URL:'))
    current = URL
    display_current_site(current)  

    return current

def goBack(current, bck, fwd):
    '''
    if bck is empty it will return a display error that says 'Cannot go back' else goBack simply gets the current site and pushes the site to the fwd stack and the new current site is popped from the bck stack and from there it will display the new current site 
    Inputs:current, bck, fwd
    Returns:current which is just the current location of the sites
    '''    
    
    if bck.isEmpty():
        display_error("Cannot go back.")
        
    else:
        fwd.push(current) 
        current = bck.pop()  
        display_current_site(current)    
            
            
    return current       
    

def goForward(current, bck, fwd):
    '''
    if fwd is empty it will return a display error that says 'Cannot go forward' else goForward simply gets the current site and pushes the site to the bck stack and the new current site is popped from the fwd stack and from there it will display the new current site 
    Inputs:current, bck, fwd
    Returns:current which is just the current location of the sites
    '''    
    if fwd.isEmpty():
        display_error("Cannot go forward.")
        
    else:
        bck.push(current) 
        current = fwd.pop()  
        display_current_site(current)  
            
    return current      

def main():
    HOME = 'www.cs.ualberta.ca'
    back = stack.Stack()
    fwd = stack.Stack()
    current = HOME
    quit = False

    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)
        display_buttons(back, fwd)


        move_cursor(0, 20)
        display_hint("Use <, > to navigate, = to enter a URL, q to quit")
        print_location(5, 5, "Action: ")
        move_cursor(13, 5)
        action = input()
        if action == '=':
            current = goToNewSite(current, back, fwd)
        elif action == '<':
            current = goBack(current, back, fwd)
        elif action == '>':
            current = goForward(current, back, fwd)
        elif action == 'q':
            clear_screen()
            quit = True
        else:
            display_error('Invalid action!')
  

if __name__ == "__main__":
    main()