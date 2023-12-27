from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Welcome to Pong Game")
screen.tracer(0)
player=Paddle()
opponent=Paddle()
opponent.goto(x=-350,y=0)
ball=Ball()
score=Score()
screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")
screen.onkey(opponent.move_up,"w")
screen.onkey(opponent.move_down,"s")
game_is_on=True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor()>285 or ball.ycor()<-285:
        ball.ybounce()
    if ball.distance(player)<50 and ball.xcor()>320 or ball.distance(opponent)<50 and ball.xcor()<-320:
        ball.xbounce()
        ball.ball_speed*=0.95
    if ball.xcor()>390:
        score.l_scores()
        ball.reset_position()
    if ball.xcor()<-390:
        score.r_scores()
        ball.reset_position()



screen.exitonclick()