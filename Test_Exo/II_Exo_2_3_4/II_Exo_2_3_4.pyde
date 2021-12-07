from random import*
def setup():
    size(800,800)
    background (randint(0,50),randint(130,190),randint(50,200))
def draw():

    mini_moi(mouseX,mouseY)
    
def mini_moi(x,y):
        fill(160,150,100)
        ellipse(x,y,200,200)
        fill(255)
        ellipse(x-10,y-30,5,15)
        fill(255)
        ellipse(x+20,y-30,5,15)
        fill(0)
        line(x-20,y+40,x+20,y+40)

        

    
    