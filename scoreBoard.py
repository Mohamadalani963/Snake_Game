from turtle import Turtle
class Scoreboard(Turtle) :
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()

        self.goto(0, 270)
        self.updateScoreBoard()
        self.hideturtle()

    def updateScoreBoard(self):
        self.write(f"score: {self.score}", align="center",font={"Arial", 24, "normal"})

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",font={"Arial", 24, "normal"})
    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreBoard()


