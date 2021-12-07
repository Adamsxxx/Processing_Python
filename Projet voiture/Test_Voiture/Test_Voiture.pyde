x=0
y = 100.0
speed = 1.0

def setup():
  size(400, 400)

def draw():
  background(255)
  move()
  car(x,y)

def move():
  global x
  x = x + speed
  if x > width:
          x = 0

def car(x,y):
  fill(0)
  rect(x+50, 50, 30, 10)
  ellipse(x+40,50,20,45)
