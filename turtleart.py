import turtle
from random import randint
import pygame

# Music section 
pygame.mixer.init()
pygame.mixer.music.load('space.mp3')
pygame.mixer.music.play(-1)

# Inital initalisation
height, width = 1400, 1000
my_wn = turtle.Screen()
turtle.setup(height, width)
turtle.bgcolor('black')


def hazzy_ball():
    turtle.speed(8)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])
  
    starting_position = (randint(-600,600), randint(-400,400))
    
    turtle.penup()  
    turtle.goto(starting_position)  
    turtle.pendown() 

    for x in range(100):
        turtle.forward(200)
        turtle.left(175)

def cloud_ball():
    turtle.speed(100)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])
    starting_position = (randint(-600,600), randint(-400,400))
    
    turtle.penup()  
    turtle.goto(starting_position)  
    turtle.pendown() 
    
    for i in range(180):
        turtle.forward(200)
        turtle.right(61)
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.right(61)
        turtle.forward(200)
        turtle.right(181)
   
    
        

def spikey():
    turtle.speed(5)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])
    starting_position = (randint(-600,600), randint(-400,400))
    
    turtle.penup()  
    turtle.goto(starting_position)  
    turtle.pendown()  
    for x in range(13):
        turtle.forward(100)
        turtle.left(150)

def black_hole():
    starting_position = (randint(-600,600), randint(-400,400))
    turtle.speed(30)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])
    turtle.penup()  
    turtle.goto(starting_position)  
    turtle.pendown()  
    for i in range(50):
        turtle.circle(2*i)
        turtle.circle(-2*i)
        turtle.left(i)
    turtle.exitonclick()

def simple_star(amount):
    turtle.speed(5)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])
    for a in range(amount):
        starting_position = (randint(-600,600), randint(-400,400))
        turtle.penup()  
        turtle.goto(starting_position)  
        turtle.pendown() 
        for a in range(5):
            turtle.forward(10)
            turtle.right(144)

def small_star(amount):
    turtle.speed(10)
    turtle.pencolor('white')
    for a in range(amount):
        starting_position = (randint(-600,600), randint(-400,400))
        turtle.penup()  
        turtle.goto(starting_position)  
        turtle.pendown() 
        for a in range(5):
            turtle.forward(5)
            turtle.right(144)

def small_star_colour(amount):
    turtle.speed(5)
    colour = randint(0,5)
    colour_choice = ['cyan', 'red', 'yellow', 'purple', 'green', 'magenta']
    turtle.pencolor(colour_choice[colour])

    for a in range(amount):
        starting_position = (randint(-600,600), randint(-400,400))
        turtle.penup()  
        turtle.goto(starting_position)  
        turtle.pendown() 
        for a in range(5):
            turtle.forward(5)
            turtle.right(144)


def spiral():
    turtle.speed(10)
    starting_position = (randint(-600,600), randint(-400,400))
    turtle.pencolor('green')
    turtle.penup()  
    turtle.goto(starting_position)  
    turtle.pendown()
    h=9
    while h <= 38:
        turtle.circle(h)
        h += 9
    n=10
    while n <= 40:
        turtle.circle(n)
        n += 10
    g=11
    while g <= 44:
        turtle.circle(g)
        g += 11



small_star_colour(randint(3, 20))
small_star(randint(5, 25))
simple_star(randint(5, 25))

if randint(0,5) % 2 == 0:
    spiral()
    hazzy_ball()
else:
    spikey()
    black_hole()
    


cloud_ball()
