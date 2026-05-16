from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(rpaddle.go_up, "Up")
screen.onkeypress(rpaddle.go_down, "Down")
screen.onkeypress(lpaddle.go_up, "w")
screen.onkeypress(lpaddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


    if ball.xcor() > 320 and abs(ball.ycor() - rpaddle.ycor()) < 50:
        ball.setx(320)
        ball.bounce_x()


    if ball.xcor() < -320 and abs(ball.ycor() - lpaddle.ycor()) < 50:
        ball.setx(-320)
        ball.bounce_x()

    # Right player misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    # Left player misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()