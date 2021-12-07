i=185
j=425
x=-50
y=200
w=None
c=None
p=-200
m=300
k=1


def setup():
    global v,w,c
    size(1163,651)
    v=loadImage('fd.png')
    w=loadImage('bdf.PNG')
    c=loadImage('bdf2.PNG')

def draw():
    global v,i,j,w,x,y,c,p,m,k
    background(v)
    image(w,x,y)
    x=x+4
    if x>1200:
        y=200 
        x=-50
    Mario(i,j,k)
    image(c,p,m)
    p=p+3.5
    if p>1200:
        m=300 
        p=-150
    


def keyPressed():
    global i,k,j
    if key=='<':
        i=i-4
        j=j+4
        k=1
    if key=='q':
        i=i-4
        k=1
    if key=='a':
        i=i-4
        j=j-4
        k=1
    if key=='z':
        j=j-4
    if key=='s':
        j=j+4
    if key=='e':
        i=i+4
        j=j-4
        k=0
    if key=='c':
        i=i+4
        j=j+4
        k=0
    if key=='d':
        i=i+4
        k=0

    
def Mario(i,j,k):
    noStroke()                      #pas de contour
    fill(255,0,0)                   #couleur rouge
    rect(i+10,j-10,10,10)           #corps rouge
    rect(i+25,j-10,15,5)            #épaule droite
    rect(i+25,j-5,5,5)              #bas épaule droite
    rect(i,j-45,30,5)               #casquette haut
    rect(i-k*10,j-40,40,5)          #casquette bas
    fill(241,172,89)                #couleur visage
    rect(i+33,j-5,7,20)             #bras droit
    rect(i,j-35,30,25)              #visage
    fill(0,0,255)                   #couleur bleue
    rect(i+20,j-5,5,5)              #bretelle
    fill(255,255,0)                 #couleur bouton
    rect(i+20,j-10,5,5)             #bouton droit*
    fill(255,255,255)               #couleur gants*
    rect(i+32,j+10,7,5)             #gant droit
    fill(0,0,255)
    rect(i,j,30,30)                 #corps
    fill(0,0,255)
    rect(i,j+30,8,16)               #pied droit
    fill(0,0,255)
    rect(i+22,j+30,8,16)            #pied gauche
    fill(90,50,3)
    rect(i-7,j+46,15,6)             # chaussure droite
    fill(90,50,3)
    rect(i+23,j+46,15,6)            # chaussure gauche
    fill(255,0,0)
    rect(i,j-5,5,5)                 # carre rouge gauche
    fill(0,0,255)
    rect(i+5,j-5,5,5)               # carre bleu gauche
    fill(255,255,0)
    rect(i+5,j-10,5,5)              # carre jaune gauche
    fill(255,0,0)
    rect(i-10,j-10,15,5)            # bras gauche
    fill(241,172,89)
    rect(i-10,j-5,5,15)             # bras gauche
    fill(241,172,89)
    rect(i-10,j-5,7,15)             # bras gauche
    fill(255,255,255)
    rect(i-10,j+10,7,5)             # bras gauche
    fill(0,0,0)                     #yeux
    rect(i+18,j-30,5,5)             #yeux
    rect(i+8,j-30,5,5)              #yeux
