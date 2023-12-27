import turtle as t
class Paddle(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(5,1)
        self.color("white")
        self.penup()
        self.goto(x=350,y=0)

    def move_up(self):
        new_ycor=self.ycor()+20
        if new_ycor<290:
            self.goto(self.xcor(),new_ycor)

    def move_down(self):
        new_ycor=self.ycor()-20
        if new_ycor>-290:
            self.goto(self.xcor(),new_ycor)
