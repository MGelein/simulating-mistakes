from random import choice, random
from util import similar_looking_word, mutate_word, closest_word

class Agent:
    
    def __init__(self, simulation):
        self.simulation = simulation
        self.canonical_text = simulation.text[:]
        self.remembered_text = self.canonical_text[:]
        self.memory = simulation.sample_memory()
        self.arrogance = simulation.sample_arrogance()
        self.influence = simulation.sample_influence()
        self.vocabulary = simulation.sample_vocabulary()

    def read_word(self, word, line):
        mutated_word = mutate_word(word, line)
        if mutated_word in self.simulation.embeddings: return mutated_word
        if random() < .01: 
            return similar_looking_word(word, self.simulation.embeddings.vocab)
        return word

    def write_word(self, word):
        if word not in self.simulation.embeddings: return word
        similar_word, similarity = closest_word(word, self.simulation.embeddings)
        return similar_word if similarity > 0.9 else word

    def read(self, agent):
        read_text = []
        for line in agent.canonical_text:
            read_line = []
            joined_line = " ".join(line)
            for word in line:
                read_line.append(self.read_word(word, joined_line))
            read_text.append(read_line)
        self.remembered_text = read_text

    def write(self):
        written_text = []
        for line in self.remembered_text:
            written_line = []
            for word in line:
                written_line.append(self.write_word(word))
            written_text.append(written_line)
        self.canonical_text = written_text

