# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui
# initialize global variables used in your code
random_guess = 0
remaining_guess = 0
play100 = 1

# helper function to start and restart the game
def new_game():
    frame.start()
    range100()

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts  
    global random_guess,remaining_guess,play100
    remaining_guess=7
    random_guess=random.randrange(0, 100)
    play100=1
    print "New Game: Range is from 0 to 100"
    print "Number of remaining guesses is",remaining_guess
    print

def range1000():
    # button that changes range to range [0,1000) and restarts   
    global random_guess,remaining_guess,play100
    remaining_guess=10
    random_guess=random.randrange(0, 1000)
    play100=0
    print "New Game: Range is from 0 to 1000"
    print "Number of remaining guesses is",remaining_guess
    print

    
def input_guess(guess):
    # main game logic goes here	
    my_guess=int(guess)
    global remaining_guess
    remaining_guess-=1
    
    print "Guess was",my_guess
    print "Number of remaining guesses is",remaining_guess
    if(my_guess==random_guess): 
        print "Correct!"
        print
        if(play100==1): range100()
        else: range1000()
    elif(my_guess<random_guess): print "Higher!"
    else: print "Lower!"
    print
    if(remaining_guess==0):
        print "You Lose! Play again"
        print
        if(play100==1): range100()
        else: range1000()

    
# create frame
frame = simplegui.create_frame("Silly Guess Number", 300, 200)


# register event handlers for control elements
frame.add_button("Range is [0,100)", range100, 180)
frame.add_button("Range if [0,1000)", range1000, 180)
frame.add_input('Enter your guess', input_guess, 170)


# call new_game and start frame
new_game()


# always remember to check your completed program against the grading rubric
