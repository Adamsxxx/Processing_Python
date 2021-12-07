i=0
dx=3
j=0
dy=4
def setup ():
    size(400,400)            #Définition de la Taille du fond d'ecran
    background(15,157,232)   #Couleur du fond d'écran (R;V;B) Jusqu'a 255

def draw ():
    global i,dx,j,dy
    background(15,157,232)
    fill(15,7,107)       #Choix de la couleur de la figure géométrique.
    mini_moi(i,j) # Position(x;y) puis Taille (Horizontale;Verticale)
    i=i+dx
    j=j+dy
    if i>400:
        dx=-dx
    if i<0:
        dx=-dx
    if j>400:
        dy=-dy
    if j<0:
        dy=-dy
        
def mini_moi(x,y):
        fill(160,150,100)
        ellipse(x,y,200,200)
        fill(255)
        ellipse(x-10,y-30,5,15)
        fill(255)
        ellipse(x+20,y-30,5,15)
        fill(0)
        line(x-20,y+40,x+20,y+40)