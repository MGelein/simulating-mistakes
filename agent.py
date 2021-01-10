class Agent:
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.text = simulation.text[:]

    def read(self, text):
        read_text = []
        for line in text:
            read_line = []
            for word in line:
                read_line.append(word)
            read_text.append(read_line)
        self.text = read_text

    def write(self):
        written_text = []
        for line in self.text:
            written_line = []
            for word in line:
                written_line.append(word)
            written_text.append(written_line)
        return written_text
