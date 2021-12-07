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


def draw():
    global i,j
    Mario(i,j,k)

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
    rect(i+33,j+10,7,5)             #gant droit
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
