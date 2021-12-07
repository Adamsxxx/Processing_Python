from random import*

L=[]
m=millis()
x=46
y=775
dx=0
dy=0

def setup():
    size(800,960)
    background(121,28,248)
def draw():
    global x,y,dy,dx
    background(121,28,248)
    global m 
    for i in range(len(L)):
        ellipse(L[i][0],L[i][1],20,20)
        L[i][1]=L[i][1]+1
    t=randint(2500,5000)
    print (m)
    if millis()-m>t:
        L.append([randint(0,799),0])
        m=millis()
    x=x+1*dx
    y=y-1*dy
    if y>473:
        dy=0
    if x>950:
        dx=0
    if y<37:
        dy=0
    if x<45:
        dx=0
    mini_moi(x,y)
def mini_moi(x,y):
    fill(251,252,250)
    ellipse(x-22.5,y+160,40,40)
    ellipse(x+22.5,y+160,40,40)
    fill(88,41,0)
    rect(x-107.5,y+75,60,5)
    rect(x+47.5,y+75,60,5)
    fill(255,255,255)
    ellipse(x,y,75,75)
    fill(0)
    ellipse(x-10,y-5,10,10)
    ellipse(x+10,y-5,10,10)
    line(x-10,y+25,x+10,y+20)
    fill(251,252,250)
    ellipse(x,y+92.5,100,110)
    fill(88,41,0)
    fill(223, 109, 20)
    triangle(x,y+7.5,x,y+17.5,x-20,y+12.5)
    
    

    
def keyPressed():
    global x
    if key==CODED:
        if keyCode==RIGHT and x<745 :
            x=x+15
        if keyCode==LEFT and x>60 :
            x=x-15
    global y
    if key==CODED:
        if keyCode==UP and y<775:
            if y>473:
                y=y-13
        if keyCode==DOWN and y>775:
            y=y+13
            
