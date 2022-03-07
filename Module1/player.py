
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
FONT = ("comic sans", 20, "normal")


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("arrow") #Shape from Turtle in this case is a arrow
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup() # Picks the pen up so the item does not draw a line as it moves
        self.go_to_start()
        self.setheading(90) #Sets the orientation of the item to angle

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

class ScoreLevel(Turtle):


    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle() #hide the item
        self.penup() #Picks the pen up so the turtle does not draw a line as it moves
        self.goto(-280, 250)
        self.update_scorelevel()

    def update_scorelevel(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT) #Font of the text

    def increase_level(self):
        self.level += 1
        self.update_scorelevel()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)