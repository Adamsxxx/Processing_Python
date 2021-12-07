from random import*
def setup():
    size(400,400)
    background (randint(0,255),randint(0,255),randint(0,255))

def draw():
    if mousePressed==True:
        fill(randint(0,255),randint(0,255),randint(0,255))
    ellipse(mouseX,mouseY,20,20)
    
    