# Player class with score system
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def add_score(self, points):
        self.score += points

    def show_score(self):
        print(f"{self.name}'s Score: {self.score}")

player = Player("Sova")
player.add_score(50)
player.show_score()