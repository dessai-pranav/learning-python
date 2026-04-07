import random
from turtle import Turtle, Screen

screen = Screen()
all_turtles = []
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230,y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! the winning turtle is {winning_color} color")
            else:
                print(f"You lose! the winning turtle is {winning_color} color")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()