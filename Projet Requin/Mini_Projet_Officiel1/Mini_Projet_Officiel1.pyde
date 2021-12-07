from random import*
x=0
y=90
z=1

i=0
j=465

k=0
l=600

m=1400
n=500
b=1

u=725
r=515
a=1
t=1

def setup():
    size(1400,700)  #(1400,700)
    
def draw():
    rectMode(CORNER)
#De base pour le ciel il aurait été mieu de faire un Simple Linear Gradient mais incompréhension de la fonction lerpColor()...
    background(255)  #38,196,236
    
    #Le Ciel () <3
    fill(21,120,255,230)
    rect(0,0, 1400, 420)
    fill(21,120,255,230)
    rect(0,0, 1400, 450)
    
    #LA MER  () <3
    
    fill(38,196,236,220)
    rect(0,450, 1400, 400)
    fill(38,196,236,30)
    rect(0,550, 1400, 400)
    
    
    
    
    global i,b                  #L'ON GLOBALISE 
    global z,k,l,m,n,j
    global a,r,u,t
    global x
    Nuage(x,y)                 #On affiche 
    Speed()                    #On le fait bouger 

    

    
     #REQUIN Rapide:
    
    Requin(i,j)
    
    if i>1400:     #requin qui va faire une trajectoire rectiligne et a partir de i=900 dessendre a j=600 pour continuer sa trajectoire
        i=0        
    i=i+3

    if i>900:      #ICI IL VA SE REMETTRE A I + 0 ET J + 465 QUAND IL AURA DEPASSER J=900 CAR IL AURA DISPARUT DE L'ECRAN SINON...
        j=j+1
        if j>900:
            j=465 
            i=0
                

        
   #Requin Lent:  ( )
     
    if k>1400:
        k=0
    k=k+1.25
    Requin(k,l)
    
    mini_moi(u,r)
    
    #LE REQUIN2 : ( )
        
    Requin2(m,n)
    
    if m<0:
        m=1400
    m=m-2
    
    #Pivotement du REQUIN2 ( )
    n=n+b
    if n<=500 :       
        b=0.5
        
    if n>650:
        b=-0.5
    


    
#CONSTRUCTION DES DEUX REQUIN 

def Requin(x,y):
    fill(142, 162,198)
    arc(x,y,65,90,PI+HALF_PI,PI+PI,PIE)
    
    
    
def Requin2(x,y):
    fill(140, 165,198)
    arc(x,y,65,90,PI,HALF_PI+PI,PIE)
    
    
    
    
# def  keyPressed():
    # global i 
    # if key=='s':
    #     i=i+1
    # if key=='z':
    #     i=i-1

#VITESSE DU NUAGE 

def Speed():
    global x
    x=x+z
    if x>1300:
        x=-200
    
#CONSTRUCTION DU NUAGE  

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
    
    
    #Verification 
    
    print (v,j)
    
v="j="
  
  
  #VOILA TERMINER JOYEUX NOEL ET BONNE ANNEE ....
  
  
  #personnage    
  
def mini_moi(u,r):
    stroke(0)
    ellipseMode(CENTER)
    fill(175,110,70)
    ellipse(u,r-63,50,50)
    rectMode(CENTER)
    stroke(0)
    rect(u,r,50,75)
    rect(u+35,r-5,20,65)
    rect(u-35,r-5,20,65)
    rect(u+15,r+65,20,65)
    rect(u-15,r+65,20,65)
  
#maillot de bain
    fill(175,0,70)
    ellipse(u-12*t,r-25,20,15)
    ellipse(u+12*t,r-25,20,15)
    triangle(u-10*t,r+30*t,u*t,r+40*t,u+10*t,r+30*t)
    
#Canard    
    fill(275,150,0)
    rectMode(CENTER)
    rect(u,r,95,20)
    rect((u+50*a)+t,r-27,20,75)
    ellipse((u+58*a)+t,r-65,35,35)
    
    noStroke()
#commande        
def keyPressed():
    global a,r,u,t
    if key==CODED:
        if keyCode==RIGHT and u<1400 : #Pour aller a droit jusqua la limite x=1400
            u=u+10
            a=1
            t=1
        if keyCode==LEFT and u>0: #Pour aller a gauche jusqua la limite x=0
            u=u-10
            a=-1 
            t=1
        if keyCode==UP and r>470:#Pour aller en haut jusqu'a la limite y=470
            r=r-10
            t=1500
            
        if keyCode==DOWN and r<700: #Pour aller en bas jusqu'a la limite y=700
            r=r+10
            a=0
            t=1
            
