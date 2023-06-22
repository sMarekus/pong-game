from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

right_home_position = (350, 0)
left_home_position = (-350, 0)

right_paddle = Paddle(right_home_position)
left_paddle = Paddle(left_home_position)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.home()
        ball.bounce_x()
        scoreboard.l_point()
        right_paddle.goto(right_home_position)
        left_paddle.goto(left_home_position)
        ball.move_speed = 0.1
    elif ball.xcor() < -380:
        ball.home()
        ball.bounce_x()
        scoreboard.r_point()
        right_paddle.goto(right_home_position)
        left_paddle.goto(left_home_position)
        ball.move_speed = 0.1

screen.exitonclick()