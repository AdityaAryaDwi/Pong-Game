from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,False,"center",("Courier",60,"normal"))
        self.goto(100,200)
        self.write(self.r_score,False,"center",("Courier",60,"normal"))

    def l_scores(self):
        self.l_score+=1
        self.update_score()
    def r_scores(self):
        self.r_score+=1
        self.update_score()