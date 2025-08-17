# Inheritance demo with Agents
class Agent:
    def __init__(self, name):
        self.name = name

class Duelist(Agent):
    def role(self):
        print(f"{self.name} is a Duelist.")

jett = Duelist("Jett")
jett.role()