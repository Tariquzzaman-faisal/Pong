from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.speedX = 2
        self.speedY = 2
        self.moveSpeed = 0.1
    def move(self):
        currX = self.xcor()
        currY = self.ycor()
        self.goto(currX + self.speedX, currY + self.speedY)
    def bounceY(self):
        self.speedY *= -1
    def bounceX(self):
        self.speedX *= -1
        self.moveSpeed *= 0.5
    def reset(self):
        self.moveSpeed = 0.01
        self.goto((0, 0))
        self.bounceY()
