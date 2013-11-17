# implementation of card game - Memory

import simplegui
import random

cards = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7]
exposed = []
firstcard = 0 
secondcard = 0
state = 0
counter = 0
# helper function to initialize globals
def new_game():
    global cards, exposed, counter
    random.shuffle(cards)
    exposed = [False] * 16
    counter = 0
    label.set_text("Turns = " + str(counter))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, firstcard, secondcard, counter
    if state==0:
        firstcard = pos[0]/50
        exposed[firstcard] = True
        state = 1
    elif state == 1:
        secondcard = pos[0]/50
        exposed[secondcard] = True
        state = 2
    else:
        if(cards[firstcard] != cards[secondcard]):
            exposed[firstcard] = False
            exposed[secondcard] = False
        firstcard = pos[0]/50
        exposed[firstcard] = True
        state = 1
        counter += 1
        label.set_text("Turns = " + str(counter))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(16):
        if(exposed[i] == False):
            canvas.draw_line(((50*i+25), 0), (50*i+25,100), 50, 'Green')
            canvas.draw_line(((50*i+49), 0), (50*i+49,100), 3, 'Black')
        else: canvas.draw_text(str(cards[i]), (50*i+10, 70), 60, 'White')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric