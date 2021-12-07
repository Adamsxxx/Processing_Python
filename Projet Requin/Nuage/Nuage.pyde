from random import*
x=0
y=90
z=1    #Vitesse du Nuage qui defile


def setup():
    size(1400,700)
    
def draw():
    
    background(38,196,236)
    
    Nuage(x,y)
    Speed()
    
#JE NE COMPREND PAS POURQUOI LA GRADUATION DU X SES INVERSER  A DROITE IL EST EGALE ~ "-200" Et A DROITE IL EST EGALE A ~1200 ??
def Speed():
    global x
    x=x+z
    if x>1300:
        x=-200
    


def Nuage(x,y):
    fill(255,252,252)
    noStroke();
    ###1
    ellipse(1200-x,90,200,90)
    ###2
    ellipse(1230-x,90,90,105)
    ###3
    ellipse(1175-x,90,90,110)
    ###4
    ellipse(1272-x,90,40,75)
    ###5
    ellipse(1130-x,90,40,75)
    
    print (v,x)
    
v="x="
    
 
