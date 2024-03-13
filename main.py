from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import winsound

screen = Screen()

screen.colormode(255)
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor(48, 56, 56)
# tracer method controls the animation on the screen, put 0 to turn off the animation
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

r_paddle.color(25, 172, 81)
l_paddle.color(191, 51, 68)

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "u")
screen.onkey(l_paddle.go_down, "d")

# whenever you turn off the animation , manually update the screen & refresh it every single time
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce if it hits the wall
        ball.bounce_y()
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        winsound.PlaySound("Pong_bounce.wav", winsound.SND_ASYNC)

    # detect when right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect when left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
