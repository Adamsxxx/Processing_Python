i=0
j=0
def setup():
    size(300,300)
    
def draw():
    global i,j
    background(175, 167, 123)
    fill(240, 195, 0)
    ellipse(50+j,50+i,10,10)
    
def keyPressed():
    global i,j
    if key =='up':
        i=i+5
    if key== 'z':
        i=i-5
    if key =='d':
        j=j+5
    if key=='q':
        j=j-5
