from turtle import Turtle

""" A class to display current score and game over message """


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.write_score()

    # Update and write the score
    def write_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", False,
                   align="center", font=("Arial", 25, "normal"))

    # Print the message after the game is over
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", False, align="center",
                   font=("Arial", 25, "normal"))
