# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
status = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.inventory = []	# create Hand object

    def __str__(self):
        s = "Hand Contains "	# return a string representation of a hand
        for card in self.inventory:
            s = s + card.suit + card.rank + " "
        return s
        
    def add_card(self, card):
        self.inventory.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        val = 0
        hasA = False
        for card in self.inventory:
            val += VALUES.get(card.rank)
            if(card.rank == 'A'): hasA = True
        if(hasA and val + 10 <= 21): val += 10
        return val
            
    def draw(self, canvas, pos):
        i = 0
        for card in self.inventory:
            card.draw(canvas, [pos[0] + i * CARD_SIZE[0] + i * 10, pos[1]])
            i += 1
        
# define deck class 
class Deck:
    def __init__(self):
        self.inventory = []	# create a Deck object
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.inventory.append(card)

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.inventory)    # use random.shuffle()

    def deal_card(self):
        return self.inventory.pop(len(self.inventory)-1)	# deal a card object from the deck
    
    def __str__(self):
        s = "Deck Contains "	# return a string representation of a hand
        for card in self.inventory:
            s = s + card.suit + card.rank + " "
        return s



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, deck, status, score
    if(in_play): 
        outcome = "You give up so you LOSE!"
        score -= 1
        in_play = False
    else:
        outcome = ""
        status = "Stand or Hit ?"
        in_play = True
        player = Hand()
        dealer = Hand()
        deck = Deck()
        deck.shuffle()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
  

def hit():
    # if the hand is in play, hit the player
    global in_play, player, score, outcome, status
    val = 0
    if(in_play):
        player.add_card(deck.deal_card())
        val = player.get_value()
        status = "Stand or Hit ?"
    # if busted, assign a message to outcome, update in_play and score
    if(val > 21): 
        score -= 1
        in_play = False
        outcome = "More than 21, You LOSE!"
        status = "Play Again? Hit Deal button"
    
def stand():
    global in_play, dealer, deck, player, score, outcome, status
    if(not in_play): status =  "You already lose"
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while(dealer.get_value() < 17):
            dealer.add_card(deck.deal_card())
        if(dealer.get_value() > 21):
            score += 1
            outcome = "You WIN!!!"
            status = "Congrats! Play again and win MORE"
        elif(player.get_value() > dealer.get_value()):
            score += 1
            outcome = "You WIN!!!"
            status = "Congrats! Play again and win MORE"
        else:
            score -= 1
            outcome = "You LOSE!!!"
            status = "Play Again? Hit Deal button"
        in_play = False
        
    # assign a message to outcome, update in_play and score
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, in_play, outcome, status
    canvas.draw_text('Black Jack', (170, 80), 60, 'Black')
    canvas.draw_text("Score = " + str(score), (500, 100), 20, 'Red')
    canvas.draw_text("Dealer's cards", (50, 170), 30, 'White')
    canvas.draw_text("Your cards", (50, 370), 30, 'White')
    canvas.draw_text(outcome, (300, 170), 20, 'White')
    canvas.draw_text(status, (300, 370), 15, 'White')
    player.draw(canvas, (50, 400))
    dealer.draw(canvas, (50, 200))
    if(in_play): canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [86.5,250], CARD_SIZE)

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric