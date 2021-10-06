from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.p1 = 0
        self.p2 = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.p2, False,  "center", ("Courier", 60, "normal"))
        self.goto(100, 200)
        self.write(self.p1, False, "center", ("Courier", 60, "normal") )
    
    def increaseP1(self):
        self.p1 += 1
        self.update()

    def increaseP2(self):
        self.p2 += 1
        self.update()
