import turtle

def MyName():
    window=turtle.Screen()
    window.bgcolor("lightgreen")

    turtle.pendown()
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)

def Square():

    window=turtle.Screen()
    window.bgcolor("lightgreen")

    turtle.pendown()
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(79)
    turtle.penup()

    window.exitonclick()

def Triangle():
    window=turtle.Screen()
    window.bgcolor("lightgreen")

    turtle.pendown()
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.right(45)
    turtle.forward(100)
    turtle.penup()

    window.exitonclick()

def Hexagon():
    window=turtle.Screen()
    window.bgcolor("AntiqueWhite1")

    turtle.pendown()

    while i<6:
        turtle.forward(100)
        turtle.right(120)
        i += 1



def Rand(X):
    print("The day of the week today is " + X)