import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()


player1 = Paddle(350, 0)
player2 = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()
screen.onkey(player1.moveUp, "Up")
screen.onkey(player1.moveDown, "Down")

screen.onkey(player2.moveUp, "w")
screen.onkey(player2.moveDown, "s")

GameON = True
while GameON:
    time.sleep(ball.moveSpeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()
    if ball.xcor() > 340 and ball.distance(player1) < 50:
        ball.bounceX()
        player1.playerSpeedup()
    elif ball.xcor() < -340 and ball.distance(player2) < 50:
        ball.bounceX()
        player2.playerSpeedup()
    if ball.xcor() > 360:
        ball.reset()
        player2.playerResetSpeed()
        scoreboard.increaseP2()
    elif ball.xcor() < -360:
        ball.reset()
        player1.playerResetSpeed()
        scoreboard.increaseP1()

screen.exitonclick()
