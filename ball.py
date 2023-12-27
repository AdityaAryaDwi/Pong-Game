from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed=0.1
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xvar=10
        self.yvar=10
    
    def move(self):
        new_xcor=self.xcor()+self.xvar
        new_ycor=self.ycor()+self.yvar
        self.goto(new_xcor,new_ycor)

    def ybounce(self):
        self.yvar*=-1

    def xbounce(self):
        self.xvar*=-1

    def reset_position(self):
        self.goto(0,0)
        self.xbounce()
        self.ball_speed=0.1