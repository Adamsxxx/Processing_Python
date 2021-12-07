y=0
v=None
x=0

def setup():
    global v
    size(400,400)
    v=loadImage('nuage.png')
    

def draw():
    global y,x,v
    y=y+1
    x=x+2
    background(202,234,252)
    fill(252,252,0)
    noStroke()
    ellipse(200,y,80,70)
    fill(0,127,255)
    noStroke()
    rect(0,300,400,100)
    image(v,x,150)
    if x>450:
        x=-100




#def mer():
#    fill(0,127,255)
#    rect(0,300,400,100)
    
#def soleil():
#    fill(252,252,0)
#    ellipse(200,y,80,70)
# def nuage():



    