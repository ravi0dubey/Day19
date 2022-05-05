from turtle import Turtle,Screen

kachua = Turtle()
screen = Screen()

kachua.speed(200)


kachua.shape("turtle")
def move_forwards():
    kachua.forward(10)

def move_backwards():
    kachua.backward(10)

def clear_drawing():
    # kachua.clear()
    kachua.reset()

def move_counter_clockwise():
    kachua.circle(120,180)

def move_clockwise():
    kachua.circle(-120, 180)

def move_counter_clockwise():
    kachua.circle(120,180)

def move_clockwise():
    kachua.circle(-120, 180)


screen.listen()
screen.onkey(move_forwards,"W")
screen.onkey(move_backwards,"S")
screen.onkey(move_counter_clockwise,"A")
screen.onkey(move_clockwise,"D")
screen.onkey(clear_drawing,"C")

screen.exitonclick()
