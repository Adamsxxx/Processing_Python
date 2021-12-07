x=575
y=325
def setup():
    size(1163,651)


def draw():
    global x,y
    background(0,0,0)
    noStroke()
    fill(0,0,255)
    rect(x,y,30,30) # corps
    fill(0,0,255)
    rect(x,y+30,8,16) #pied droit
    fill(0,0,255)
    rect(x+22,y+30,8,16)#pied gauche
    fill(90,50,3)
    rect(x-7,y+46,15,6)# chaussure droite
    fill(90,50,3)
    rect(x+23,y+46,15,6)# chaussure gauche
    fill(255,0,0)
    rect(x,y-5,5,5)# carre rouge gauche
    fill(0,0,255)
    rect(x+5,y-5,5,5)# carre bleu gauche
    fill(255,255,0)
    rect(x+5,y-10,5,5)# carre jaune gauche
    fill(255,0,0)
    rect(x-10,y-10,15,5)# bras gauche
    fill(241,172,89)
    rect(x-10,y-5,5,15)# bras gauche
    fill(241,172,89)
    rect(x-10,y-5,7,15)# bras gauche
    fill(255,255,255)
    rect(x-10,y+10,7,5)# bras gauche
    