#turtel2
#Henri Lepik
#09.03.22

import turtle

#aken
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Liigutame kilpkonna!")

def viisnurk(pikkus):
    t = turtle.Turtle()
    for v in range (5):
        t.forward(100)
        t.left(-144)
        
viisnurk(100)

kolmnurklong= input("sisesta kolmnurga kylje pikkus: ")
kolmnurkvarv= input("sisesta kolnurga värv: ")

def kolmnurk(pikkus):
    t=turtle.Turtle()
    for i in range (3):
        t.forward(pikkus)
        t.left(-120)

kolmnurk(100)

turtle.exitonclick()
