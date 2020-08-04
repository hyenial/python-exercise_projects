import turtle

def draw_square(some_turtle):
    for i in range(6):
        some_turtle.forward(100)
        some_turtle.right(60)

def draw_art():

    brad = turtle.Turtle("turtle")
    brad.color("yellow")
    brad.speed(2)

    for i in range(30):
        draw_square(brad)
        brad.right(12)

window = turtle.Screen()
window.bgcolor("blue")

draw_art()

window.exitonclick()