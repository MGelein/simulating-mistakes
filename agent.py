class Agent:
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.text = simulation.text[:]

    def read(self, text):
        self.text = text

    def write(self):
        return self.text
