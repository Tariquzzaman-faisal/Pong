from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, X, Y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.constX = X
        self.constY = Y
        self.goto((X, Y))
        self.shapesize(5, 1)
        self.paddleSpeed = 10

    def moveUp(self):
        currX = self.xcor()
        currY = self.ycor()
        self.goto(currX, currY + self.paddleSpeed)

    def moveDown(self):
        currX = self.xcor()
        currY = self.ycor()
        self.goto(currX, currY - self.paddleSpeed)
    def playerSpeedup(self):
        self.paddleSpeed *= 2

    def playerResetSpeed(self):
        self.paddleSpeed = 10
        self.goto((self.constX, self.constY))
