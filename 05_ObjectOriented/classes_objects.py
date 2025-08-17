# Class and object example
class Agent:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability

    def show(self):
        print(f"{self.name} has ability: {self.ability}")

agent1 = Agent("Jett", "Tailwind")
agent1.show()