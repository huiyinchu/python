# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
count=0
x=0
y=0
milsec = "0"
stopped = True
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global milsec
    milsec = str(t % 10);
    t /= 10;
    sec2 = t % 60
    sec = str(sec2)
    if(sec2 < 10): sec = "0" + sec
    t /= 60
    mins = str(t)
    return mins + ":" + sec + ":" + milsec
    

def format2():
    return str(x) + "/" + str(y)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global stopped
    stopped = False
    timer.start()  

def stop():
    global stopped 
    timer.stop()
    if(not stopped):
        global x,y
        y += 1
        if(milsec == "0"): x += 1
    stopped = True
    
def reset():
    global count, x, y
    count=0
    x=0
    y=0
    timer.stop();

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1
    

# define draw handler
def draw(canvas):
    canvas.draw_text(str(format(count)), [125, 100], 24, "White")
    canvas.draw_text(str(format2()), [260, 20], 20, "white")
# create frame
frame = simplegui.create_frame("Text drawing", 300, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, tick)
button1 = frame.add_button('start', start, 50)
button2 = frame.add_button('stop', stop, 50)
button2 = frame.add_button('reset', reset, 50)

# start frame
frame.start()


# Please remember to review the grading rubric
