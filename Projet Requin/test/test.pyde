
from random import*
x=50
y=50

def setup():
    
    size(200,200)
    background(38,196,236)

    
    
    
def draw():
    global x,y
    
    background(randint(0,255,),randint(0,255),randint(0,255))
    frameRate(30)
    ellipse(mouseX,mouseY,40,40)
    # if x<0:
    #     x=400

    # x=x-1
    

    
