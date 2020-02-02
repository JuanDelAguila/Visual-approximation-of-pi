import random

diameter = 950
window_size = 1000
radius = diameter/2
padding = (window_size-diameter)/2
total = 0
x = 0
y = 0
inside = 0

def setup():
    size(window_size, window_size)
    background(0)
    fill(0)
    stroke(255)
    rect(padding,padding,diameter,diameter)
    ellipse(width/2,height/2,diameter,diameter)
    

def draw():
    global total, inside
    total += 1.0
    translate(width/2,height/2)
    generate_random_coordinates()
    calculate_distance()
    pi = 4*(inside)/(total)
    if total/100.0 == int(total/100):
        print(pi)
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    fill(r,g,b)
    stroke(r,g,b)
    ellipse(x,y,20,20)
    

def generate_random_coordinates():
    global x, y
    x=random.uniform(-radius,radius)
    y=random.uniform(-radius,radius)
    
        
def calculate_distance():
    global iterations, inside, x, y
    distance = ((x-0)**2+(y-0)**2)**0.5
    if distance <= radius:
        inside += 1.0
