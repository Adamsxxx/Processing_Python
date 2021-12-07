i=0
dy=3
def setup():
    size(400,400)


def draw():
    global i,dy
    background(20,12,248)
    mini_moi(200,i)
    i=i+dy
    if i>350:
        dy=-dy
    if i<0:
        dy=-dy
    
        
def mini_moi(x,y):
    fill(244,10,10)
    ellipse(x,y,100,100)
    fill(106,178,251)
    ellipse(x-20,y-20,15,15)
    ellipse(x+20,y-20,15,15)
    strokeWeight(3)
    line(x-20,y+20,x+20,y+20)