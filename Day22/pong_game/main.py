from turtle import Screen

from pong_game.ball import Ball
from pong_game.paddle import Paddle
import time

from pong_game.scoreboard import Scoreboard

game_is_on = True
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() < 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()

    # Detect collision when right paddle misses the ball
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
    # Detect collision when left paddle misses the ball
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
    # Detect the winner
    if scoreboard.l_score == 1:
        scoreboard.winner = "left"
        scoreboard.announce_winner(scoreboard.winner)
        game_is_on = False
    if scoreboard.r_score == 1:
        scoreboard.winner = "right"
        scoreboard.announce_winner(scoreboard.winner)
        game_is_on = False
screen.exitonclick()
