from turtle import Turtle, Screen
import random

kachua1 = Turtle()
kachua2 = Turtle()
kachua3 = Turtle()
kachua4 = Turtle()
screen = Screen()
screen.setup(500,400)
colors =["red","green","blue","yellow","magenta","pink"]
y_cord =[0,-20,-40,20,40,60]
all_turtles = []

game_continue = False
user_guess = screen.textinput(title= "Make your bet", prompt="Which turtle will win the race? Enter a color:")

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_cord[turtle_index])
    all_turtles.append(new_turtle)

if user_guess:
    game_continue = True

while game_continue:
    for turtles in all_turtles:
        pace = random.randint(0, 10)
        turtles.forward(pace)
        if turtles.xcor() >= 230:
            game_continue = False
            winning_color = turtles.pencolor()
            if winning_color == user_guess:
                print(f"You have won!!! {winning_color} turtle is  the winner")
            else:
                print(f"You have lost!!! {winning_color} turtle is  the winner")




screen.exitonclick()
