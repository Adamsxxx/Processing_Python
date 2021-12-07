from random import*

L=[]
m=millis()

def setup():
    size(800,960)
    
def draw():
    global m
    background(121,121,121)
    
    for i in range(len(L)):
        ellipse(L[i][0],L[i][1],20,20)
        L[i][1]=L[i][1]+1
    t=randint(250,500)
    print (m)
    if millis()-m>t:
        L.append([randint(0,799),0])
        m=millis()
