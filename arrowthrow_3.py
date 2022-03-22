# hw5-2.py
# Date: 11th March, 2022
# Author: Anjan Rana Magar


from graphics import *
from math import sqrt

# a. we define these upfront so that they can be called later!
number_of_arrows = 0 
circle_list = [] # a.i. We need this to make the citcle move later
dx = 0.5 # a.ii. the speed of the board moving
dart_list = [] #a.iii| we move the dart(arrow) as well so that both arrow and board looks like they are sticking to each other.
message_score = Text(Point(5,-20), "Total score") # a.iv. this is just to label it.
entryBox = Entry(Point(20,-20), 10) # a.v. This is a entry box for the score
score = 0 # ''' defining things outside of function makes it a global variable, but you need to say global inside the funciton as well.'''

def animationLoop(win):
    global dx
    global score
    while(1):
        for circle in circle_list:
            circle.move(dx,0)
        for dart in dart_list:
            dart.move(dx,0)
        reference_cicle = circle_list[0]
        get_x_coords = reference_cicle.getCenter().x
        if get_x_coords >=30 or get_x_coords <=-30: #''' This is to make sure when the circle hit -30 on board, it returns back: for that
                                                    # of course we need to have. '''
            dx=-dx
        mouse = win.checkMouse()
        if (mouse and number_of_arrows > 0):
            addDart(mouse,win)
        
def addDart(p,win):
    print('aaa')
    global number_of_arrows
    global score
    number_of_arrows-=1
    dart_circ = Circle(p,0.5)
    dart_circ.setFill("green")
    dart_list.append(dart_circ)
    dart_circ.draw(win)
      # finding the distance
    distance_a = int(sqrt((p.getX()-circle_list[0].getCenter().x)**2+p.getY()**2))
    # print(distance_a)
    
        #ii. compare the distance to total score.
    if distance_a < 2:
        score = score+10
    elif distance_a <4:
        score = score+8
    elif distance_a <6:
        score = score+6
    elif distance_a <8:
        score = score+4
    elif distance_a <10:
        score = score+2
    # print("You score is ",score)

    
    entryBox.setText(score)


def main():
    # 1. create window
    win = createwindow()
    entryBox.setText(score)
    entryBox.draw(win)

    message_score.setSize(15)
    message_score.draw(win)
    

    global number_of_arrows
    # 2. ask for number arrow and get the number, 
    number_of_arrows = arrownum_get(win) 
    #print(num_assign)
    

    # 3. looping to limit the number of points:

    animationLoop(win)
    entryBox.draw(win)
           
    print("You score is ",score)
    

def createwindow():
    win = GraphWin("archery_anjan", 600,600)
    win.setCoords(-40,-40,40,40)
    win.setBackground("white")
    '''creating an archery'''
    white_a = Circle(Point(0,0),10)
    white_a.setFill("white")
    white_a.draw(win)
    black_a = Circle(Point(0,0),8)
    black_a.setFill("black")
    black_a.draw(win)
    blue_a = Circle(Point(0,0),6)
    blue_a.setFill("skyblue")
    blue_a.draw(win)
    red_a = Circle(Point(0,0),4)
    red_a.setFill("red")
    red_a.draw(win)
    yellow_a = Circle(Point(0,0),2)
    yellow_a.setFill("yellow")
    yellow_a.draw(win)
    circle_list.append(white_a)
    circle_list.append(black_a)
    circle_list.append(blue_a)
    circle_list.append(red_a)
    circle_list.append(yellow_a)
    return win

def arrownum_get(win):
    
    entryBox = Entry(Point(7,35), 15)
    entryBox.setText(" 3")
    entryBox.draw(win)

    message = Text(Point(-10,35), "Number of arrows:")
    message.setSize(15)
    message.draw(win)

    messageBackground = Rectangle(Point(-3,32), Point(4,28))
    messageBackground.setFill("grey")
    messageBackground.draw(win)
    
    done_message = Text(Point(0.5,30), "Done")
    done_message.setSize(12)
    done_message.draw(win)
    
    win.getMouse()
    
    getnum = int(entryBox.getText()) # we will use this later

    entryBox.undraw()
    message.undraw()
    messageBackground.undraw()
    done_message.undraw()

    
##    entryBox = Entry(Point(20,-20), 15)
##    entryBox.setText("0")
##    entryBox.draw(win)
##
##    message_score = Text(Point(5,-20), "Total score")
##    message_score.setSize(15)
##    message_score.draw(win)
    
    return getnum

    
main()


