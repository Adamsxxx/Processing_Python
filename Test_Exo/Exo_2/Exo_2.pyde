
#Le principe de cette algorithme va etre de faire apparaitre une figure géométique a l'infinie qui aura une couleur fixé dans une position (x,y) aléatoire allant de 0 a 399
from random import*  
def setup():
    size(400,400)
    background(randint(0,255),randint(0,255),randint(0,255))
    frameRate(5)
def draw():
    fill(244,102,27)
    background(randint(0,255),randint(0,255),randint(0,255))
    ellipse(randint(0,399),randint(0,399),20,20)